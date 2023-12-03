#!/usr/bin/python3
import socket

host = input("Digite o nome do host: ")
portas_str = input("Digite a lista de portas separadas por vírgula: ")

# Divida a string de portas em uma lista
portas = [int(p) for p in portas_str.split(',')]

for porta in portas:
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(1)  # Defina um timeout para a tentativa de conexão
    try:
        meusocket.connect((host, porta))
        banner = meusocket.recv(1024)
        print(f"A porta {porta} está aberta no {host}:")
        print(banner.decode('utf-8'))
    except socket.error as e:
        print(f"A porta {porta} está fechada no {host}: {e}")
    finally:
        meusocket.close()

