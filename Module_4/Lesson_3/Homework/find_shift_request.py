import json
from urllib.parse import unquote_plus

from flask import Flask, request

app = Flask(__name__)


def find_shift(iterable: list[int]) -> int:
    shift = len(iterable) - iterable.index(min(iterable))
    return shift


@app.route("/find-shift/", methods=["POST"])
def find_shift_encoding() -> tuple[str, int]:
    form_data = request.get_data(as_text=True)

    if request.content_type == "application/x-www-form-urlencoded":
        request_data = unquote_plus(form_data)

        numbers = list(map(int, request_data.split("=", maxsplit=1)[1].split(",")))

    elif request.content_type == "application/json":
        request_data = json.loads(form_data)

        numbers = []

        for key in request_data:
            numbers.extend(request_data[key])

    else:
        return "Unsupported content type", 400

    return f"Shift: {find_shift(numbers)}", 200


if __name__ == "__main__":
    app.run(debug=True)
