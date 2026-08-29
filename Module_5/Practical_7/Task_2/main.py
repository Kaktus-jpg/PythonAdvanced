import shlex
import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired

app = Flask(__name__)


class Form(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(
        filters=[lambda sec: int(sec) if 0 < int(sec) < 30 else 0],
        validators=[InputRequired()],
    )


@app.route("/run-program/", methods=["POST"])
def run_program() -> tuple[str, int]:
    form = Form()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data

        if not (str(timeout).isdigit() and 0 < timeout < 30):
            return "timeout must be between 0 and 30 seconds", 400

        quote_code = shlex.quote(code)

        raw_cmd = f"prlimit --nproc=1:1 python -c {quote_code}"
        command = shlex.split(raw_cmd)

        program = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )

        try:
            program.wait(timeout=timeout)
            stdout, stderr = program.communicate()
            stdout = str(stdout.decode())
            stderr = str(stderr.decode())

        except subprocess.TimeoutExpired:
            stderr = program.communicate()[1]
            stderr = str(stderr.decode())

            return f"Исполнение кода не уложилось в необходимое время<br>{stderr}", 400
        else:
            if program.returncode == 0:
                return stdout, 200
            else:
                return (
                    f"Программа закончилась с кодом {program.returncode}<br>{stderr}",
                    400,
                )

    return f"Invalid input {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
