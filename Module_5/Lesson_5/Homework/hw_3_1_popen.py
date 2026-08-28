import shlex
import string
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def _ps():
    arguments: list[str] = request.args.getlist("arg")
    arguments_cleaned = [shlex.quote(arg) for arg in arguments]
    command_str = f"ps {' '.join(arguments_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.Popen(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()

    result.kill()

    return string.Template("<pre>${output}</pre>").substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
