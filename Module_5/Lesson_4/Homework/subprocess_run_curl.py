import re
import shlex
import subprocess


def curl_request():
    command = shlex.split(
        'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'
    )
    res = subprocess.run(command, capture_output=True)

    output = res.stdout.decode()

    ip = re.search(r'{"ip":"(?P<ip>\d+\.\d+\.\d+\.\d+)"}', output)

    if ip:
        print(ip.group("ip"))
    else:
        print("Something went wrong.")


if __name__ == "__main__":
    curl_request()
