from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://127.0.0.1:5001"
ORDER_SERVICE_URL = "http://127.0.0.1:5002"

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API Gateway!"})

@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": f"User service not reachable: {e}"}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        response = requests.get(f"{ORDER_SERVICE_URL}/orders")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": f"Order service not reachable: {e}"}), 500

@app.route('/user_orders/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    try:
        user_response = requests.get(f"{USER_SERVICE_URL}/users")
        order_response = requests.get(f"{ORDER_SERVICE_URL}/orders")

        users = user_response.json()
        orders = order_response.json()

        user = next((u for u in users if u["id"] == user_id), None)
        if not user:
            return jsonify({"message": "User not found"}), 404

        user_orders = [o for o in orders if o["user_id"] == user_id]

        return jsonify({
            "user": user,
            "orders": user_orders
        })
    except Exception as e:
        return jsonify({"error": f"Error connecting services: {e}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
