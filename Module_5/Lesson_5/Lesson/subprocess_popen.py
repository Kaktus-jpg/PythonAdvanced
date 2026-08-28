import subprocess


def simple_popen():
    p = subprocess.Popen(["uv", "run", "test_program.py"])
    return p


if __name__ == "__main__":
    res = simple_popen()
