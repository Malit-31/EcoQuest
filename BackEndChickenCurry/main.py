from flask import Flask, request, jsonify
from flask import json
from flask_cors import CORS

#freddy fazbear's pizzaria har har har har har har har har har
#freddy fazbear's pizzaria har har har har har har har har har

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

if __name__ == "__main__":
    app.run()
