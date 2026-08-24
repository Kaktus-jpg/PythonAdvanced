from collections.abc import Iterable

from flask import Flask, request

app = Flask(__name__)


def nearest_num(number: int, iterable: Iterable) -> int:
    nearest_number: int | None = None

    for num in iterable:
        if nearest_number is None:
            nearest_number = num
            continue
        elif abs(number - num) < abs(number - nearest_number):
            nearest_number = num

    return nearest_number


@app.route("/nearest-num/", methods=["GET"])
def nearest():
    list_a: list[int] = sorted(request.args.getlist("mas-a", type=int))

    num_x: int | None = request.args.get("num-x", type=int)

    return f"<h3>Nearest number: {nearest_num(num_x, list_a)}</h3>", 200


if __name__ == "__main__":
    app.run(debug=True)
