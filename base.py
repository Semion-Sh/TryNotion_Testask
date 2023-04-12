from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['database']
users = db['users']

@app.route('/create_user', methods=['POST'])
def create_user():
    user = {
        'name': 'name_test',
        'email': 'test@example.com',
        'password': '123456789'
    }
    users.insert_one(user)
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run()