# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/max_number/<path:numbers>")
# def max_number(numbers: str):
#     numbers_as_num = (int(it) for it in numbers.split("/"))
#     return f"Максимальное переданное число <i>{max(numbers_as_num)}</i>"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#

###### С Float числами


from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers: str) -> tuple[str, int]:
    numbers_split = list[str] = numbers.split("/")
    try:
        max_number: float = max(map(float, numbers_split))
        return f"Максимальное число <i>{max(max_number)}</i>", 200
    except ValueError:
        return "Переданы некорректные значения", 400


if __name__ == "__main__":
    app.run(debug=True)
