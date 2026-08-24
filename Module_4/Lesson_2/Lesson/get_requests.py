from flask import Flask, request

app = Flask(__name__)


@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: list[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return "You must specify at least one cell_tower_id", 400

    phone_prefixes: list[str] = request.args.getlist("phone_prefix")

    protocols: list[str] = request.args.getlist("protocol")

    signal_level: float | None = request.args.getlist("signal_level", type=float)

    return (
        f"Search for {cell_tower_ids} cell towers. Search criterias: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
    )


if __name__ == "__main__":
    app.run(debug=True)
