# -*- coding: utf-8 -*-
import tp3_funcoes

while True:
    print ("""
    1.Informações associadas ao processador.
    2.Informações associadas à memória.
    3.Informações associadas ao disco.
    4.Informações associadas ao IP.
    5.Estatística / Relatório
    6.Sair
    """)

    opcao = input("Escolha uma opção:")
    if opcao == 1:
        tp3_funcoes.processador()

    elif opcao == 2:
        tp3_funcoes.memoria()

    elif opcao == 3:
        tp3_funcoes.disco()

    elif opcao == 4:
        tp3_funcoes.rede()

    elif opcao == 5:
        tp3_funcoes.relatorio()

    elif opcao == 0:
        break
    else:
        print("\n Opção Inválida. Tente Novamente.")
