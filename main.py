from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/monthly-payment', methods=['POST'])
def monthly_payment():
    try:
        data = request.get_json()
        principal = data.get("principal")
        rate = data.get("rate")
        years = data.get("years")

        if not all([principal, rate, years]):
            return jsonify({"error": "All values must be provided and greater than 0"}), 400

        monthly_rate = rate / 100 / 12
        num_payments = years * 12
        monthly_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))

        return jsonify({"monthly_payment": round(monthly_payment, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
