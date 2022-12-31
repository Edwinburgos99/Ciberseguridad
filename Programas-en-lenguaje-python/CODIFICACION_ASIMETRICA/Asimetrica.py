# crear un programa donde se lea un archivo txt, mediante una llave publica encripta el texto de entrada
# y con una llave privada desencripta el texto encriptado, debido a que la libreria Crypto esta obsoleta
# lo mejor es optar por una actualizacion que te brinde lo mismo, para este caso use la libreria cryptodome
import binascii
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# genera un numero aleatorio Cryptografico para usarlo luego en las llaves 
random_generator = Crypto.Random.new().read
# genera una llave privada y publica para el programa
llave_privada = RSA.generate(1024, random_generator)
llave_publica = llave_privada.publickey()

# convertir en formato binario
llave_private = llave_privada.exportKey(format='DER')
llave_public = llave_publica.exportKey(format='DER')

# convertir de binario a formato 'utf-8'
llave_pri = binascii.hexlify(llave_private).decode('utf-8')
llave_pub = binascii.hexlify(llave_public).decode('utf-8')

# convertir de strings a RSA
private = RSA.importKey(binascii.unhexlify(llave_pri))
public = RSA.importKey(binascii.unhexlify(llave_pub))
# leyendo el contenido del archivo txt 
message = open("message.txt")
leer = (message.read())
M_encriptar = leer.encode()
# se cifra el mensaje anterior en formato RSA
# PKCS1_OAEP tipo de cifrado basado en RSA
cifrado = PKCS1_OAEP.new(public)
mensaje_encriptado = cifrado.encrypt(M_encriptar)
# Imprimiendo el mensaje encriptado en formato RSA
print(mensaje_encriptado)

decifrado = PKCS1_OAEP.new(private)
mensaje_desencriptado = decifrado.decrypt(mensaje_encriptado)
# Imprimiendo en pantalla el mensaje leido y desencripptado del txt
print(mensaje_desencriptado)