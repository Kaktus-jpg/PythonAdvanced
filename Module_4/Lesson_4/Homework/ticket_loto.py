from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField

app = Flask(__name__)


class LotoForm(FlaskForm):
    name = StringField()
    family_name = StringField()
    ticket = IntegerField()


def lucky_ticket(ticket_num: str) -> bool:
    first_three, last_three = map(int, ticket_num[:3]), map(int, ticket_num[3:])
    return sum(first_three) == sum(last_three)


@app.route("/form/", methods=["POST"])
def form():
    form = LotoForm()

    if form.validate_on_submit():
        name, family_name, ticket = (
            form.name.data,
            form.family_name.data,
            form.ticket.data,
        )

        info = {
            "name": name,
            "family_name": family_name,
            "ticket": ticket,
        }

        if not all(info.values()):
            errors_dict = {}

            for form, value in info.items():
                if value is None:
                    errors_dict[form] = f"{form} form cannot be empty."

            return f"Invalid input {errors_dict}", 400

        elif str(ticket).startswith("0") or len(str(ticket)) != 6:
            return (
                "Invalid ticket. ticket can't starts with 0 and must have 6 digits in lenght",
                400,
            )

        elif lucky_ticket(str(ticket)):
            return f"Поздравляем вас, {name} {family_name}", 200

        else:
            return "Неудача. Попробуйте ещё раз!", 406


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
