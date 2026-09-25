import logging

import flask
from http_utils import get_ip_address
from subprocess_utils import get_kernel_version

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")

app = flask.Flask(__name__)


@app.route("/get_system_info")
def get_system_info():
    logger.info("Start working")
    ip = get_ip_address()
    kernel = get_kernel_version()
    return f"<p>{ip}</p><p>{kernel}</p>"


if __name__ == "__main__":
    app.run(debug=True)
