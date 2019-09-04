whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

import string
s = "What's wrong with ASCII?!?!?"

print(s.rstrip(string.punctuation))

def make_bitseq(s: str) -> str:
	if not s.isascii():
		raise ValueError("ASCII only allowed")
	return " ".join(f"{ord(i):08b}" for i in s)

print(make_bitseq("bits"))
print(make_bitseq("CAPS"))
print(make_bitseq("$25.43"))
print(make_bitseq("~5"))

def n_possible_values(nbits: int) -> int:
    return 2 ** nbits

from math import ceil, log
def n_bits_required(nvalues: int) -> int:
	return ceil(log(nvalues) / log(2))

print(n_bits_required(256))

print(int('11'))

print(int('11', base=10))

print(int('11', base=2))

print(int('11', base=8))

print(int('11', base=16))

print(0b11)

print(0o11)

print(0x11)

import locale

print(locale.getpreferredencoding())

print(all(len(chr(i).encode("ascii")) == 1 for i in range(128)))

ibrow = "🤨"

print(len(ibrow))

ibrow.encode("utf-8")
print(len(ibrow.encode("utf-8")))

data = b"\xbc cup of flour"

print(data.decode("latin-1"))

import unicodedata
print(unicodedata.name("€"))
unicodedata.lookup("EURO SIGN")