from Crypto.PublicKey import RSA

with open ('bruce_rsa.txt',) as key:

    FLG = RSA.importKey(key.read())

    

    print(FLG.n)