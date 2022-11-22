from tkinter import Button, Label, Tk

import requests


def get_quotation():
    request = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    request_dic = request.json()

    dollar = request_dic['USDBRL']['bid']
    euro = request_dic['EURBRL']['bid']
    bitcoin = request_dic['BTCBRL']['bid']

    current_quote = f'''
    Valor atual das moedas:
    Dólar: {dollar}
    Euro: {euro}
    BTC: {bitcoin}'''

    # Atribuindo valor ao campo text da cotação
    text_quote["text"] = current_quote


#   Interface gráfica
janela = Tk()

janela.title("Cotação atual das Moedas")

viewer_text = Label(
    janela, text="Clique no botão para ver as cotações das moedas")
# Posição do item na janela
viewer_text.grid(column=0, row=0, padx=10, pady=5)

button = Button(janela, text="Buscar cotações", command=get_quotation)
button.grid(column=0, row=2, padx=10, pady=10)

text_quote = Label(janela, text="")
text_quote.grid(column=0, row=1, padx=10, pady=5)

janela.mainloop()
