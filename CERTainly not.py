from asn1crypto.x509 import Certificate

with open ('2048b-rsa-example-cert.der','rb') as key:
    
    file = Certificate.load(key.read())

    print(file.public_key.native['public_key']['modulus'])

