import binascii

from pwn import xor

decrypt = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

format = 'crypto{'

key = xor(decrypt, format)  

key2 = 'myXORkey'
fullkey = (key2 * (len(decrypt)))

FLG = xor (fullkey, decrypt)

print(FLG)