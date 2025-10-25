from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"order_id": 101, "item": "Pizza", "user_id": 1, "quantity": 2, "price": 20.5, "status": "Pending"},
    {"order_id": 102, "item": "Burger", "user_id": 2, "quantity": 1, "price": 10.0, "status": "Completed"}
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.get_json()
    required_fields = ["order_id", "item", "user_id", "quantity", "price", "status"]
    if not all(field in new_order for field in required_fields):
        return jsonify({"message": "Missing fields!"}), 400
    orders.append(new_order)
    return jsonify({"message": "Order added successfully"}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
