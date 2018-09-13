from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)

with open('config.json') as json_file:
    data = json.load(json_file)
    client = MongoClient(data['mongoURI'])
db = client.get_default_database()
collection = db.logs

@app.route('/api/logs', methods=['POST'])
def post_logs():
    if not request.json or not 'data' in request.json:
        abort(400)
    collection.insert_one({"data": request.json['data']})
    return jsonify({"status": True}), 201

if __name__ == '__main__':
    app.run(debug=True) #false