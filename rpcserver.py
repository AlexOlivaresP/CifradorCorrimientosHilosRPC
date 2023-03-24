
import xmlrpc.server

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

server = xmlrpc.server.SimpleXMLRPCServer(("192.168.92.128", 3012))
print("Esperando consultas de cifrado...")

server.register_function(cifrado, "cifrado")

server.serve_forever()

