from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: list[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return "You must specify at least one cell_tower_id", 400

    elif not all(tower_id > 0 for tower_id in cell_tower_ids):
        return "cell_tower_ids can't be less than 0", 400

    phone_prefixes: list[str] = request.args.getlist("phone_prefix")
    for phone_prefix in phone_prefixes:
        if not (
            phone_prefix.endswith("*")
            and 1 < len(phone_prefix.removesuffix("*")) <= 10
            and phone_prefix.removesuffix("*").isdigit()
        ):
            return "phone_prefixes is wrong", 400

    protocols: list[str] = request.args.getlist("protocol")
    if not all(protocol in ("2G", "3G", "4G") for protocol in protocols):
        return "protocols can be only 2G, 3G or 4G", 400

    signal_level: float | None = request.args.getlist("signal_level", type=float)

    date_from: str | None = request.args.get(key="date_from")

    if date_from:
        date_from_date = datetime.strptime(date_from, "%Y%m%d")
        if not date_from_date:
            return "Invalid date for date_from", 400
    else:
        date_from_date = None

    date_to: str | None = request.args.get(key="date_to")
    if date_to:
        date_to_date = datetime.strptime(date_to, "%Y%m%d")
        if not date_to_date:
            return "Invalid date for date_to", 400
    else:
        date_to_date = None

    if date_to_date and date_from_date:
        try:
            assert date_from_date < date_to_date
        except AssertionError:
            return "date_to must be more than date_from", 400

    return (
        f"Search for {cell_tower_ids} call towers. Search criterias: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}, "
        f"date_from={date_from}, "
        f"date_to={date_to}"
    )


if __name__ == "__main__":
    app.run(debug=True)
