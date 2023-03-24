# CifradorCorrimientosHilosRPC
Cifrador de corrimientos que usa hilos y RPC para ejecutar en un servidor en una maquina en una red local.

Este codgigo funciona de la siguiente manera:

HilosVm es el raiz y tambien es el archivo local, en este archivo podras modificar la ruta del archivo de texto que quieras cifrar.

El servidor se inicia con rpcserver.py que este te ayudara a poder tener un servicio de escucha en el puerto 3312 o el que decidas mediante protocolo RPC.

Despues de inicializado tendras que cambiar la IP de tu servidor y correr el programa que te entregara los tiempos en cluster y tiempos en local.
