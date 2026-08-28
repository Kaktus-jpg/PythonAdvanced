import subprocess


def run_program():
    command = "sleep 10 && exit 1"

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )

    print(f"Process 1 started. PID {process.pid}")

    process.wait()

    if process.returncode == 1:
        print(f"Process with PID {process.pid} ended successfully (with code 1)")


if __name__ == "__main__":
    run_program()
