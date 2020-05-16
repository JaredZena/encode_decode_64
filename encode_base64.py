import base64
import sys

def encode():
    plain = sys.argv[1]
    print('encoded code is: ')
    print(base64.b64encode(plain.encode()))


if __name__ == "__main__":
    encode()
