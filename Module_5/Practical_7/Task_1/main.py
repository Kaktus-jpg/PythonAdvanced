import os
import shlex
import signal
import subprocess
import time

from flask import Flask

app = Flask(__name__)


@app.endpoint("hello")
def hello_world():
    return "Hello World!"


def start_server(port: int = 5000, timeout: float = 1):
    command = shlex.split(f"lsof -i :{shlex.quote(str(port))}")

    get_processes = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
    )
    stdout, stderr = get_processes.communicate()

    all_output = stdout.decode().split("\n")
    headings = all_output[0].split()

    processes = all_output[1:]

    formatted_procs = []

    for output in processes:
        if output:
            values = tuple(output.strip().split())

            process = dict(zip(headings, values))
            formatted_procs.append(process)

    for process in formatted_procs:
        pid = int(process["PID"])

        try:
            os.kill(pid, signal.SIGTERM)

            deadline = time.monotonic() + timeout

            while time.monotonic() < deadline:
                try:
                    os.kill(pid, 0)
                    time.sleep(0.1)
                except ProcessLookupError:
                    # process с pid завершён
                    break

            # process с pid не завершился за timeout секунд, отправляется SIGKILL
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            print(f"PID {pid}: процесс уже завершён")
        except PermissionError:
            print(f"PID {pid}: недостаточно прав")
        except OSError as exc:
            print(f"PID {pid}: системная ошибка: {exc}")

    app.run(port=port)


if __name__ == "__main__":
    start_server(5000)
