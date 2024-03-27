from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config["MONGO_URI"] = "mongodb+srv://yashl:saad@cluster0.duk6cmy.mongodb.net/myDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/store', methods=['POST'])
def store():
    name = request.json['name']
    email = request.json['email']
    mongo.db.users.insert_one({'name': name, 'email': email})
    return jsonify(message="Data stored successfully"), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
