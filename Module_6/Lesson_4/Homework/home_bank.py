import csv
import logging

from flask import Flask
from werkzeug.exceptions import InternalServerError

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.route("/bank_api/<branch>/<int:person_id>")
def bank_api(branch: str, person_id: int):
    branch_card_file_name = f"bank_data/{branch}.csv"

    with open(branch_card_file_name, "r") as fi:
        csv_reader = csv.DictReader(fi, delimiter=",")

        for record in csv_reader:
            if int(record["id"]) == person_id:
                return record["name"]
        return "Person not found", 404


@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError):
    original: Exception | None = getattr(e, "original_exception", None)

    if isinstance(original, FileNotFoundError):
        logger.exception(
            f"Unable to access {original.filename}\n",
            exc_info=original,
        )

    elif isinstance(original, OSError):
        logger.exception(
            "Unable to access a card\n",
            exc_info=original,
        )

    return "Internal Server Error", 500


if __name__ == "__main__":
    app.run()
