import codecs
import base64
import urllib.parse


# Hex
def hexDecode(arg):
    return bytes.fromhex(arg).decode("UTF-8")

def hexEncode(arg):
    return codecs.encode(arg, "hex_codec").decode("UTF-8")


# Rot13
def rot13Decode(arg):
    return codecs.decode(arg, "rot_13")

def rot13Encode(arg):
    return codecs.encode(arg, "rot_13")


# base64
def base64Decode(arg):
    return base64.b64decode(arg).decode("UTF-8")

def base64Encode(arg):
    return base64.b64encode(bytes(arg.encode())).decode()


# URL
def urlEncode(arg):
    return urllib.parse.quote(str)

def urlDecode(arg):
    return urllib.parse.unquote(str)
