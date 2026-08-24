import sys


def decrypt(encryption: str) -> str:
    """Расшифровывает сообщение по правилам одной и двух точек"""
    result = []
    dots = 0
    for symbol in encryption:
        if symbol != ".":
            result.append(symbol)
            dots = 0
            continue
        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0
    return "".join(result)


if __name__ == "__main__":
    data = sys.stdin.read()
    print(decrypt(data))
