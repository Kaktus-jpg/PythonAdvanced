import subprocess
import time


def run_ten_processes():
    start = time.time()
    command = 'sleep 15 && echo "My mission is done here!"'

    processes = []
    for proc in range(1, 11):
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(f"Process number {proc} started. PID {process.pid}")
        processes.append(process)

    for process in processes:
        process.wait()

        if b"done" in process.stdout.read() and process.returncode == 0:
            print(f"Process with PID {process.pid} ended successfully")

    print("Done in", time.time() - start)


if __name__ == "__main__":
    run_ten_processes()
