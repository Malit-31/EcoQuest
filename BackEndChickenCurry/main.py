from flask import Flask, request, jsonify
from flask import json
from flask_cors import CORS


userdataPath = "freddyFazbear.json"
app = Flask(__name__)
CORS(app)

@app.route('/savedata', methods=['POST'])
def saveData():
    send = request.get_json()
    with open(userdataPath, 'r') as f:
        filedata = json.load(f)
    for user, data in send.items():
        if user not in filedata:
            data["points"] = 0  # Initialize points for new users
        else:
            data["points"] = filedata[user]["points"]  # Preserve existing points
    filedata.update(send)
    with open(userdataPath, 'w') as f:
        json.dump(filedata, f)
    return jsonify({"status": "posted"}) 


@app.route('/login', methods=['GET'])
def login():
    result = request.args.get('total').split(",")  # "name,password"
    with open(userdataPath,'r') as file:
        data = json.load(file)
    if result[0] in data:
        if result[1] == data[result[0]]['password']:
            return jsonify({"status":"success"})
        return jsonify({"status":"wrong password"})
    return jsonify({"status":"wrong username"})

@app.route('/addpoints', methods=['POST'])
def add_points():
    request_data = request.get_json()
    username = request_data.get("username")
    points_to_add = request_data.get("points")

    with open(userdataPath, 'r') as f:
        filedata = json.load(f)

    filedata[username]['points'] += points_to_add

    with open(userdataPath, 'w') as f:
        json.dump(filedata, f)

    return jsonify({"message": f"Added {points_to_add} points to {username}"}), 200

@app.route('/getpoints', methods=['GET'])
def get_points():
    username = request.args.get('username')

    with open(userdataPath, 'r') as f:
        filedata = json.load(f)

    points = filedata[username].get('points', 0)

    return jsonify({"username": username, "points": points}), 200


if __name__ == "__main__":
    app.run()