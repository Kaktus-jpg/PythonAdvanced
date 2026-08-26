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


@app.route("/registration", methods=["POST"])
def registration() -> tuple[str, int]:
    form = RegisterForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}", 200

    return f"Invalid inputm {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
