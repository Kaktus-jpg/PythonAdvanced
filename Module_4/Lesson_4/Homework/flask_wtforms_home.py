import re

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField

app = Flask(__name__)


class RegisterForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
    index = IntegerField()
    comment = StringField()


def check_name_format(name: str, pattern: str | None = None) -> bool:
    pattern = pattern or r"[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.\s[А-ЯЁ]\."
    return bool(re.fullmatch(pattern, name))


@app.route("/registration", methods=["POST"])
def registration() -> tuple[str, int]:
    form = RegisterForm()

    if form.validate_on_submit():
        email, phone, address, name = (
            form.email.data,
            form.phone.data,
            form.address.data,
            form.name.data,
        )

        main = {
            "email": email,
            "phone": phone,
            "address": address,
            "name": name,
        }

        if not all(main.values()):
            errors_dict = {}

            for form, value in main.items():
                if value is None:
                    errors_dict[form] = f"{form} form cannot be empty."

            return f"Invalid input {errors_dict}", 400

        elif len(str(phone)) != 10:
            return "Invalid input. phone form must have 10 digits.", 400

        elif not check_name_format(name):
            return (
                "Invalid input. name form must be like this pattern: Фамилия И. О.",
                400,
            )

        else:
            return f"Successfully registered user {email} with phone +7{phone}", 200

    return f"Invalid input {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
