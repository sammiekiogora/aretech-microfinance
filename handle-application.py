from flask import Flask, request, jsonify
app = Flask(__name)

loans = []

@app.route('/apply_loan', methods=['POST'])
def apply_loan():
    data = request.get_json()
    customer_name = data['customer_name']
    amount = data['amount']
    interest_rate = data['interest_rate']
    duration = data['duration']

    loan = Loan(customer_name, amount, interest_rate, duration)
    loans.append(loan)

    return jsonify({"message": "Loan application submitted successfully."}), 201

if __name__ == '__main__':
    app.run(debug=True)
