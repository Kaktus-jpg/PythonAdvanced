import subprocess


def get_processes_count():

    res = subprocess.run(["ps", "-A"], capture_output=True)

    output = res.stdout.decode()

    processes_count = output.count("\n") - 1

    print("Количество запущенных процессов:", processes_count)


if __name__ == "__main__":
    get_processes_count()
