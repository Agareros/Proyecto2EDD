import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

import pyasn1




class encriptar:
    
    def generar(self):
        #generar las llaves
        print "encriptando"
        #llave_publica,llave_privada =pyasn1.newkeys(512)

    def __init__(self):
        self.generar()



#    def encriptar(mensaje,llave_publica):
 #       try:
  #          mensaje_encriptado=rsa.encrypt
        
xa=encriptar()

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message:', encrypted #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print 'decrypted', decrypted

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()