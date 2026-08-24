from itertools import product

from flask import Flask, request

app = Flask(__name__)


@app.route("/unity-nums/", methods=["GET"])
def unity():
    list_a: list[int] = request.args.getlist("mas-a", type=int)
    list_b: list[int] = request.args.getlist("mas-b", type=int)

    combinations = ""
    for combination in product(list_a, list_b):
        combinations += f"{combination}<br>"

    return combinations


if __name__ == "__main__":
    app.run(debug=True)
