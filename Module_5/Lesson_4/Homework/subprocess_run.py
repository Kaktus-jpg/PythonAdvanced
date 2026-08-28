import subprocess
import sys


def run_program():
    res = subprocess.run(["uv", "run", "test_program.py"], stdout=sys.stderr)
    print(res)


if __name__ == "__main__":
    run_program()
