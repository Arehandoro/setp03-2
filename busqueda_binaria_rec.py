#UNIVERIDAD DE SANTIAGO DE CHILE
#Carrera:  Licenciatura en Ciencias de la Computación.
#Asignatura:  Lenguaje y Técnicas de Programación.
#Profesor:  Igor Caracci.
#Ayudante:  Andrés Caro Q.
#Autor del Programa:  Alejandro Alberto Sánchez Iturriaga.
#Problema 01 - Búsqueda Binaria:

#Función de Búsqueda Binaria de forma Recursiva.
def busqueda_binaria(lista, principio, final, clave):
    if (principio <= final):    #Si la posición inicial es menor o igual a la final sigue buscando la palabra en forma recursiva.
        centro = (principio + final) // 2    #Se guarda la posición central.
        if lista[centro] == clave:    #Si la palabra que esta en la posición central es igual a la buscada, nos retorna su posición.
            return centro    #Retorna su posición en la lista.
        elif lista[centro] < clave:    #Si la palabra buscada es mayor que la de la posición central, busca en la lista las palabras mayores que ella, osea acota el intervalo de busqueda a la derecha.   
            return busqueda_binaria(lista, centro+1, final, clave)    #Se llama a si misma la función enviando el nuevo intervalo.
        else:    #Si la palabra buscada es menor que la de la posición central, busca en la lista las palabras menores que ella, osea acota el intervalo de busqueda a la izquierda. 
            return busqueda_binaria(lista, principio, centro-1, clave)    #Se llama a si misma la función enviando el nuevo intervalo. 
    else:
        return -1    #Retorna un valor que no representa ninguna posición en la lista, osea caso que no encuentra la palabra.

print("BUSQUEDA BINARIA - FUNCIÓN RECURSIVA\n")
nombre = input("Ingrese el Nombre del Archivo:  ")    #Lee el nombre del Archivo.
f = open(nombre, "r", encoding="utf-8")    #Abre el archivo y lo guarda en la variable "f".
cadena = f.read()    #Guarda todo el contenido del archivo retornado en string en cadena.
lista = cadena.split()    #La función split() retorna una lista conteniendo las subcadenas en las que se divide nuestra cadena al dividirlas por los espacios en blancos y salto de lineas.
lista = sorted(lista)    #Ordena la lista de menor a mayor, para utilizar la búsqueda binaria.
f.close()    #Cierra el archivo.
clave = input("Ingrese la Palabra a buscar:  ")    #Lee la palabra a buscar en la lista.
posicion = busqueda_binaria(lista, 0, len(lista)-1, clave)    #Llama a la función recursiva y nos retorna la posición de la palabra.
if (posicion >= 0):    #Si la posición donde esta la palabra es mayor igual a cero, osea encontro la palabra, nos imprime su posición.
    print("\nLa Palabra ("+clave+") se encuentra en la Lista, en la posición",posicion)
else:
    print("\nLa Palabra ("+clave+") no se encuentra en la Lista.")
