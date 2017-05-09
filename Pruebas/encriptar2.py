import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('Saludos, voy a ser encriptado 6', 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message:', encrypted #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()



#decrypted code below

f = open('encryption.txt', 'r')
#message = f.read()
f.close()
print "desencriptando"
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print 'TextDesencriptado->', decrypted

d = open ('encryption.txt', 'w')
#d.write(str(message))
d.write(str(decrypted))
d.close()