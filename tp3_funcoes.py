# -*- coding: utf-8 -*-
import psutil
import platform
import socket

info_memoria = psutil.virtual_memory()
info_cpu = psutil.cpu_percent(interval=1)
info_disco = psutil.disk_usage('.')
info_hostname = socket.gethostname()
info_rede = socket.gethostbyname(info_hostname)

# def processador... pegar as informações do processador
def processador():
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('          PROCESSADOR         \n')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('Uso do CPU: {} \n'.format(platform.machine()))
    print('Nome do processador: {} \n'.format(platform.processor()))
    print('Nome do computador: {} \n'.format(platform.node()))
    print('Versão do SO: {} \n'. format(platform.platform()))
    print('Sistema Operacional: {} \n'.format(platform.system()))

# def memoria (função= metodo) para pegar as infos da memoria
def memoria():
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('            MEMÓRIA           \n')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('Uso da memória: \n')
    print('Memória total: ', round(info_memoria[0] / (1024 * 1024 * 1024), 2), 'GB \n')
    print('Memória usada: ', round(info_memoria[3] / (1024 * 1024 * 1024), 2), 'GB \n')
    print('Memória livre: ', round(info_memoria[4] / (1024 * 1024 * 1024), 2), 'GB \n')

# def disco... pegar as informações do disco
def disco():
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('             DISCO            \n')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('Total: ', round(info_disco.total / (1024 * 1024 * 1024), 2), 'GB \n')
    print('Usada: ', round(info_disco.used / (1024 * 1024 * 1024), 2), 'GB \n')
    print('Livre: ', round(info_disco.free / (1024 * 1024 * 1024), 2), 'GB \n')

# def rede
def rede():
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('              REDE            \n')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    # print(f'Nome dos host: {info_hostname}')
    print('Nome do host: {} \n'.format(info_hostname))
    print('IP da rede: {} \n'.format(info_rede))

def relatorio():
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    print('          ESTATÍSTICAS        \n')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    processador()
    memoria()
    disco()
    rede()
