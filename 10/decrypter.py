import sys
import os

file = open(sys.argv[1], 'rb')
fileC = open("Decoder\\" + os.path.basename(sys.argv[1]), 'wb')

while True:
    byte = file.read(1)

    if not byte:
        break

    byte2int = (int.from_bytes(byte, sys.byteorder) - 50) % 256
    fileC.write(byte2int.to_bytes(1, sys.byteorder))

file.close()
fileC.close()
