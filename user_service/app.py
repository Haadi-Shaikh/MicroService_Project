from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25, "city": "New York"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30, "city": "San Francisco"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    required_fields = ["id", "name", "email", "age", "city"]
    if not all(field in new_user for field in required_fields):
        return jsonify({"message": "Missing fields!"}), 400
    users.append(new_user)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
