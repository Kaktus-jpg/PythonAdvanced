import shlex
import subprocess


def run_python_code_in_subprocess(code: str, timeout: int) -> tuple[str, str, bool]:
    command = f'python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    was_kill_by_timeout = False
    try:
        outs, errs = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errs = process.communicate()
        was_kill_by_timeout = True
    return outs.decode(), errs.decode(), was_kill_by_timeout


if __name__ == "__main__":
    output, _, _ = run_python_code_in_subprocess("print('hello')", 5)

    print(output)
