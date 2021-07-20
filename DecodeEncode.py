from codecs import encode
from base64 import b64encode, b64decode
from urllib.parse import quote, unquote


# Hex
def hexDecode(arg):
    return bytes.fromhex(arg).decode("UTF-8")
def hexEncode(arg):
    return encode(arg.encode(), "hex_codec").decode("UTF-8")

# Rot13
def rot13Decode(arg):
    return encode(arg, "rot_13")
def rot13Encode(arg):
    return encode(arg, "rot_13")

# base64
def base64Decode(arg):
    return b64decode(arg).decode("UTF-8")
def base64Encode(arg):
    return b64encode(arg.encode()).decode()

# URL
def urlEncode(arg):
    return quote(arg)
def urlDecode(arg):
    return unquote(arg)
