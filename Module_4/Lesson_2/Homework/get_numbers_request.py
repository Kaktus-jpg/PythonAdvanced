from math import prod

from flask import Flask, request

app = Flask(__name__)


@app.route("/numbers/", methods=["GET"])
def numbers():
    numbers_list: list[int] = request.args.getlist("number", type=int)

    nums_sum = sum(numbers_list)
    nums_multiplication = prod(numbers_list)

    return f"<h2>Sum: {nums_sum}</h2><h2>Multiplication: {nums_multiplication}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
