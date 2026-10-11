import time

from flask import Flask

app = Flask(__name__)


@app.route("/time/")
def get_time():
    moscow_time = time.gmtime(time.time() + 3 * 60 * 60)
    str_moscow_time = time.strftime("%H:%M:%S", moscow_time)
    return str_moscow_time
