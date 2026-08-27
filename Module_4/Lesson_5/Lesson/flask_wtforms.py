from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Email, InputRequired, NumberRange

app = Flask(__name__)


class RegisterForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(
        validators=[InputRequired(), NumberRange(min=10**9, max=9_999_999_999)]
    )
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField()
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration() -> tuple[str, int]:
    form = RegisterForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}", 200

    return f"Invalid input {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
