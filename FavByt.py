import binascii


decrypt = binascii.unhexlify('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')


for FLG in range(256):
    answ = ''.join(chr(b ^ FLG) for b in decrypt)

    if (answ.startswith("crypto{")):
        print(answ)
        


