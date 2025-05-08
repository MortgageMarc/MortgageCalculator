from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/monthly-payment', methods=['POST'])
def monthly_payment():
    data = request.get_json()

    try:
        principal = data['principal']
        rate = data['rate']
        years = data['years']

        monthly_rate = rate / 100 / 12
        num_payments = years * 12
        monthly_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))

        return jsonify({"monthly_payment": round(monthly_payment, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run()
