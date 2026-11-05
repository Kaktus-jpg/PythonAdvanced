import os

from flask import Flask, jsonify, make_response

APP = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000
SERVICE_NAME = os.environ.get("SERVICE_NAME", "application")
ADMIN = os.environ.get("ADMIN", "admin")


@APP.route("/hello/<user>")
def hello_user(user: str):
    return make_response(
        jsonify({"message": f"Hello from {SERVICE_NAME}, {user}! Admin: {ADMIN}"}), 200
    )


if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)
