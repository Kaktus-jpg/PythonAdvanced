from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.fields.simple import StringField
from wtforms.validators import InputRequired

from Module_6.Lesson_1.Lesson.run_in_subprocess import run_python_code_in_subprocess

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10)


@app.route("/run_code", methods=["POST"])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        stdout, stderr, killed = run_python_code_in_subprocess(
            code=code, timeout=timeout
        )
        return f"Stdout: {stdout}, Stderr: {stderr}, Process was killed by timeout: {killed}"

    return f"Bad request. Error = {form.errors}", 400


if __name__ == "__main__":
    app.run(debug=True)
