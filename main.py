from funcoes import abertura, deposito, cobranca, retiradas
import json


# Lançamento


def lancamento():
    data = input('DATA: ')
    tipo = input(
        'TIPO DE OPERAÇAO (A - Abertura) (D- Deposito) (C-Cobranca) (F-Fechamento) (T-Transferencia)(R-Retiradas): ')
    if tipo == 'A':
        valor = abertura()
    elif tipo == 'D':
        valor = deposito()
    elif tipo == 'C':
        valor = cobranca()
    elif tipo == 'R':
        valor = retiradas()
    return dict(data=data, tipo=tipo, valor=valor)


fechamento = 'NAO'

lista = []

while fechamento == 'NAO':
    fechamento = input('Deseja encerrar lançamento para fechamento da conta? Informe "SIM" ou "NAO" ')
    if fechamento == "NAO":
        lista.append(lancamento())

json_string = json.dumps(lista)
print(json_string)

with open("teste.txt", "w") as arquivo:
    conteudo = arquivo.write(json_string)

