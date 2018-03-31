"""
BINARY DECODER

Decodes both 7 and 8 bit binary
Can decipher the following also: spaces, tabs, and other whitespaces, backspaces

Madison Gay
"""
import sys
from binascii import hexlify
from binascii import unhexlify

infile = sys.stdin
covert_bin = infile.readline() #Secret message

covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    # stop at the string "EOF"
    i += 8
print("Message decoded in utf-8: ", covert)

covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 7]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    # stop at the string "EOF"
    i += 7
print("Message decoded in utf-7: ", covert)
