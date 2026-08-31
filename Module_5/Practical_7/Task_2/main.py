from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired

app = Flask(__name__)


class Form(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(
        filters=[
            lambda sec: int(sec) if str(sec).isdigit() and 0 < int(sec) < 30 else 0
        ],
        validators=[InputRequired()],
    )


@app.route("/run-program/", methods=["POST"])
def run_program() -> tuple[str, int]:
    form = Form()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data

        if not (str(timeout).isdigit() and 0 < timeout < 30):
            return "timeout must be between 0 and 30 seconds", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
