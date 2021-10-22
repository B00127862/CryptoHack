from Crypto.PublicKey import RSA

key = open('privacy_enhanced_mail.pem','r').read()

FLG = RSA.importKey(key)

print(FLG)
    
    