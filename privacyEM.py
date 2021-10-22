from Crypto.PublicKey import RSA

with open ('privacy_enhanced_mail.pem','rb') as key_file:

    FLG = RSA.importKey(key_file.read())

    

    print(FLG.d)
    
    