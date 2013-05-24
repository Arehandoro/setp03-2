#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 02 - Búsqueda Binaria Iterativa:

#Función de Búsqueda Binaria de forma Iterativa.
def busqueda_binaria(lista, clave):
    principio = 0    #Define la posición inicial de la lista.
    final = len(lista) - 1    #Define la posición final de la lista.
    while (principio <= final):    #Mientras la posición inicial sea menor o igual a la final sigue buscando la palabra en forma iterativa.
        centro = (principio + final) // 2    #Se guarda la posición central.
        if lista[centro] == clave:    #Si la palabra que esta en la posición central es igual a la buscada, nos retorna su posición.
            return centro    #Retorna su posición en la lista.
        elif lista[centro] < clave:    #Si la palabra buscada es mayor que la de la posición central, busca en la lista las palabras mayores que ella, osea acota el intervalo de busqueda a la derecha.
            principio = centro + 1    #Se guarda la posición siguiente de la central como inicial. 
        else:    #Si la palabra buscada es menor que la de la posición central, busca en la lista las palabras menores que ella, osea acota el intervalo de busqueda a la izquierda.
            final = centro - 1    #Se guarda la posición anterior de la central como final. 
    return -1    #Retorna un valor que no representa ninguna posición en la lista, osea caso que no encuentra la palabra.

print("BUSQUEDA BINARIA - FUNCIÓN ITERATIVA\n")
nombre = input("Ingrese el Nombre del Archivo:  ")    #Lee el nombre del Archivo.
f = open(nombre, "r", encoding="utf-8")    #Abre el archivo y lo guarda en la variable "f".
cadena = f.read()    #Guarda todo el contenido del archivo retornado en string en cadena.
lista = cadena.split()    #La función split() retorna una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por los espacios en blancos y salto de lineas.
lista = sorted(lista)    #Ordena la lista de menor a mayor, para utilizar la búsqueda binaria.
f.close()    #Cierra el archivo.
clave = input("Ingrese la Palabra a buscar:  ")    #Lee la palabra a buscar en la lista.
posicion = busqueda_binaria(lista, clave)    #Llama a la función iterativa y nos retorna la posición de la palabra.
if (posicion >= 0):    #Si la posición donde esta la palabra es mayor igual a cero, osea encontro la palabra, nos imprime su posición.
    print("\nLa Palabra ("+clave+") se encuentra en la Lista, en la posición",posicion)
else:
    print("\nLa Palabra ("+clave+") no se encuentra en la Lista.")
