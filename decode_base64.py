import base64
import sys

def encode():
    encoded = sys.argv[1]
    print(encoded)
    print('Decoded code is: ')
    print(base64.b64decode(encoded))


if __name__ == "__main__":
    encode()
