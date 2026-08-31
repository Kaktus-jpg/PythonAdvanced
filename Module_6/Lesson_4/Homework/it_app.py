import datetime
import json
import logging
import os
from json import JSONDecodeError

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger("account_book")

current_dir = os.path.dirname(os.path.abspath(__file__))
fixtures_dir = os.path.join(current_dir, "fixtures")

departments = {"IT": "it_dept", "PROD": "production_dept"}


class DateError(Exception):
    pass


class NameNotFoundError(Exception):
    pass


@app.route("/account/<department>/<int:account_number>/")
def sort_endpoint(department: str, account_number: int):
    dept_directory_name = departments.get(department)

    if dept_directory_name is None:
        return "Department not found", 404

    full_department_path = os.path.join(fixtures_dir, dept_directory_name)

    account_data_file = os.path.join(full_department_path, f"{account_number}.json")

    with open(account_data_file, "r") as fi:
        account_data_txt = fi.read()

    account_data_json = json.loads(account_data_txt)

    name, birth_date = account_data_json["name"], account_data_json["birth_date"]
    if not name:
        raise NameNotFoundError("Name must be a valid string!")

    day, month, year = birth_date.split(".")
    date = datetime.date(int(year), int(month), int(day))
    if not date:
        raise DateError("Date must include valid data")

    return f"{name} was born on {day}.{month}"


@app.errorhandler(DateError)
def date_error(exc: DateError) -> tuple[str, int]:
    logger.exception("Date not supported!", exc_info=exc)
    return "Internal Server Error", 500


@app.errorhandler(ValueError)
def value_error(exc: ValueError) -> tuple[str, int]:
    logger.exception("Expected day, month and year values to unpack!", exc_info=exc)
    return "Internal Server Error", 500


@app.errorhandler(NameNotFoundError)
def name_not_found_error(exc: NameNotFoundError) -> tuple[str, int]:
    logger.exception("Name not found!", exc_info=exc)
    return "Internal Server Error", 500


@app.errorhandler(KeyError)
def key_error(exc: NameNotFoundError) -> tuple[str, int]:
    logger.exception("Expected keys name and birth_date!", exc_info=exc)
    return "Internal Server Error", 500


@app.errorhandler(JSONDecodeError)
def json_decode_error(exc: JSONDecodeError) -> tuple[str, int]:
    logger.exception("JSONDecodeError", exc_info=exc)
    return "Internal Server Error", 500


@app.errorhandler(FileNotFoundError)
def file_not_found_error(exc: JSONDecodeError) -> tuple[str, int]:
    logger.exception("File not found!", exc_info=exc)

    return "Internal Server Error", 500


# Day Check, FileNotFoundError, KeyError, Month Check, json.decoder.JSONDecodeError
# ValueError, Name Check, KeyError, -, ValueError
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Started account server")
    app.run(debug=True)
