from flask import request, jsonify
from config import app, db
from user import User

@app.route("/", methods=["GET"])
def get_contacts():
    contacts = User.query.all()
    json_info = list(map(lambda x: x.json_write(), contacts))
    return jsonify({"contacts": json_info})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

