# programa que recibe de entrada un archivo de texto y muestra el resultado de la salida
# en pantalla encriptado en formato alfanumerico (letras y numeros) y con un tamaño 
# especifico dado por el usuario que representa un conjunto de datos de entrada puede ser 
# SHA256 0 SHA512

import hashlib
class HASH:
    # generamos el texto de entrada en representacion hash, gracias al metodo hexdigest 
    def generar_Hash(h):
        generar = h.hexdigest()
        return generar
l=0
# bucle que finalizara cuando l sea igual a 1
while l<1:
    # Opciones que podra seleccionar el usuario 
    print("Elige la funcion hash que prefieras para encriptar tu entrada: ")
    print("a - SHA256")
    print("b - SHA512")
    print("c - acabar el programa")
    # la ocion escogida por el usuario se guarda en una variable 
    Oescogida = input("Opcion escogida: ")

    Oescogida = Oescogida.lower()

    abrir=open("C:\\Users\\Edwin\\Desktop\\Ciberseguridad\\Programas-en-lenguaje-python\\CODIFICACION_HASH\\file.txt")
    leer = (abrir.read())

    Algoritmo = ""
    if Oescogida !='c':

        if Oescogida  == 'a':
            Algoritmo = "SHA256"
        elif Oescogida == 'b':
            Algoritmo = "SHA512"
        # formato en el que  se encriptara los datos de entrada
        bdato = bytes(leer,'utf-8')
        # se crea una nueva variable donde estara el algoritmo escogido por el usuario y los datos 
        # de entrada ya encriptados en formato 'utf-8'
        h = hashlib.new(Algoritmo,bdato)

        hash = HASH.generar_Hash(h)
        print()
        print(hash)
        print()
        l=0
    else:
        l=1
print("fin del programa")





