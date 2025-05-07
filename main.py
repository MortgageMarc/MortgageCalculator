from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/monthly-payment', methods=['POST'])
def monthly_payment():
    try:
        data = request.get_json()
        loan_amount = data.get("loan_amount")
        interest_rate = data.get("interest_rate")
        loan_term = data.get("loan_term")

        if not all([loan_amount, interest_rate, loan_term]):
            return jsonify({"error": "All values must be provided and greater than 0"}), 400

        monthly_rate = interest_rate / 100 / 12
        num_payments = loan_term * 12
        monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))

        return jsonify({"monthly_payment": round(monthly_payment, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
