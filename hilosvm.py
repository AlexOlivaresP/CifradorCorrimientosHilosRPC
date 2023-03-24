
import threading
import concurrent.futures
import time
import xmlrpc.client

def cifrado(texto,desplazamiento):
    texto = texto.upper()
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            nueva_posicion = (posicion + desplazamiento) % 27
            cifrado += alfabeto[nueva_posicion]
        else:
            cifrado += letra
    return cifrado

def decifrado(cifrado,corrimientos):
    # código que se ejecutará en el hilo
    cifrado = cifrado.upper()
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    decifrado = ""
    for letra in cifrado:
        if letra in alfabeto:
            posicion = alfabeto.find(letra)
            nueva_posicion = (posicion - corrimientos) % 27
            decifrado += alfabeto[nueva_posicion]
        else:
            decifrado += letra
    return decifrado

def vm(texto,desplazamiento):
    # Crear proxy
    print("CONECTANDO CON VM...")
    proxy = xmlrpc.client.ServerProxy("http://192.168.92.128:3012/RPC2")
    print("CONECTADO CON VM...\n")
    # Llamar función del servidor
    resultado = proxy.cifrado(texto,desplazamiento)
    # Imprimir resultado
    return resultado

#Se lee el texto a cifrar
with open("texto.txt", "r") as archivo:
    Frase = archivo.read()

Desplazamiento = int(input("Ingrese el desplazamiento: "))

#Se divide el texto en 2
mitad = len(Frase)//2
mitad1 = Frase[:mitad]
mitad2 = Frase[mitad:]

#Se ejecutan los hilos
#Crear un executor de hilos
ejecutaHilo = concurrent.futures.ThreadPoolExecutor()

#Inicia cronómetro de hilo virtual
inicio = time.time()

# Ejecutar la función en un hilo y obtener una instancia de Future
mi_hilo = ejecutaHilo.submit(vm, mitad1, Desplazamiento)
mi_hilo2 = ejecutaHilo.submit(cifrado, mitad2, Desplazamiento)

# Obtener el resultado de la función
resultado = mi_hilo.result()
resultado2= mi_hilo2.result()

fin = time.time()
tiempo_total = fin - inicio
print("Tiempo de ejecución concurrente: ", tiempo_total)

#Se guarda el texto cifrado
with open("cifrado.txt", "w") as archivo:
    archivo.write(resultado+resultado2)
print("Archivo cifrado con exito, se ha guardado en cifrado.txt")

#Inicia cronómetro de descifrado, solo con hilo local
tiempoSolo = time.time()
descif = decifrado(resultado+resultado2, Desplazamiento)
finTiempoSolo = time.time()
tiempoTotalSolo = finTiempoSolo - tiempoSolo
print("El tiempo de ejecución del descifrado únicamente con un hilo local es: ", tiempoTotalSolo, "segundos")

with open("descifrado.txt", "w") as archivo:
    archivo.write(descif)
print("Archivo descifrado con exito, se ha guardado en descifrado.txt")



