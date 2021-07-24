from hashlib import *

def Hshake_128(text, IsHex=False):
	if IsHex:
		return shake_128(bytes.fromhex(text)).hexdigest()
	return shake_128(text.encode()).hexdigest()

def Hsha224(text, IsHex=False):
	if IsHex:
		return sha224(bytes.fromhex(text)).hexdigest()
	return sha224(text.encode()).hexdigest()

def Hsha256(text, IsHex=False):
	if IsHex:
		return sha256(bytes.fromhex(text)).hexdigest()
	return sha256(text.encode()).hexdigest()

def Hblake2b(text, IsHex=False):
	if IsHex:
		return blake2b(bytes.fromhex(text)).hexdigest()
	return blake2b(text.encode()).hexdigest()

def Hmd5(text, IsHex=False):
	if IsHex:
		return md5(bytes.fromhex(text)).hexdigest()
	return md5(text.encode()).hexdigest()

def Hsha1(text, IsHex=False):
	if IsHex:
		return sha1(bytes.fromhex(text)).hexdigest()
	return sha1(text.encode()).hexdigest()

def Hsha3_384(text, IsHex=False):
	if IsHex:
		return sha3_384(bytes.fromhex(text)).hexdigest()
	return sha3_384(text.encode()).hexdigest()

def Hsha3_224(text, IsHex=False):
	if IsHex:
		return sha3_224(bytes.fromhex(text)).hexdigest()
	return sha3_224(text.encode()).hexdigest()

def Hsha3_512(text, IsHex=False):
	if IsHex:
		return sha3_512(bytes.fromhex(text)).hexdigest()
	return sha3_512(text.encode()).hexdigest()

def Hblake2s(text, IsHex=False):
	if IsHex:
		return blake2s(bytes.fromhex(text)).hexdigest()
	return blake2s(text.encode()).hexdigest()

def Hshake_256(text, IsHex=False):
	if IsHex:
		return shake_256(bytes.fromhex(text)).hexdigest()
	return shake_256(text.encode()).hexdigest()

def Hsha3_256(text, IsHex=False):
	if IsHex:
		return sha3_256(bytes.fromhex(text)).hexdigest()
	return sha3_256(text.encode()).hexdigest()

def Hsha384(text, IsHex=False):
	if IsHex:
		return sha384(bytes.fromhex(text)).hexdigest()
	return sha384(text.encode()).hexdigest()

def Hsha512(text, IsHex=False):
	if IsHex:
		return sha512(bytes.fromhex(text)).hexdigest()
	return sha512(text.encode()).hexdigest()
