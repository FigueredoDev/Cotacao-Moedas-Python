import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    contacao_atual = f'''
    Valor atual das moedas: 
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    # Atribundo valor ao campo text da cotacao
    texto_cotacao["text"] = contacao_atual


#   Interface grafica
janela = Tk()

janela.title("Cotação atual das Moedas")

texto_orientacao = Label(
    janela, text="Clique no botão para ver as cotaçẽs das moedas")
# Posição do item na janela
texto_orientacao.grid(column=0, row=0, padx=10, pady=5)

bota = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
bota.grid(column=0, row=2, padx=10, pady=10)

texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0, row=1, padx=10, pady=5)

janela.mainloop()
