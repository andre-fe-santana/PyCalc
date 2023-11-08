from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry("300x270")
root.configure(bg="grey")


visor = Frame(root, bg="green", borderwidth=1, relief="flat")
visor.place(x=5, y=5, width=290, height=50)

botoes = Frame(root, bg="grey", borderwidth=0, relief="solid")
botoes.place(x=5, y=60, width=290, height=205)


# variavel para receber os botões da calculadora
# mantém o valor da var independente

todos_valores = ''

valor_texto = StringVar() #convertendo de int para str

def mostrar_num(event):

    global todos_valores

    todos_valores = todos_valores + str(event) #concatena os valores inseridos para usar no eval depois

    valor_texto.set(todos_valores)



def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    print(resultado)

    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")


lbl_calculo = Label(visor, textvariable=valor_texto, width=14, font=("Century Gothic", 24), bg="green", fg="black",
                    justify=RIGHT, relief=FLAT, anchor="e")  # funcao de Texto (Label)
lbl_calculo.place(x=0, y=0)

#BOTÕES
#LINHA 1
btn_parentesis_abre = Button(botoes, command = lambda: mostrar_num('('),text="(", width=9, height=2, bg='orange')
btn_parentesis_abre.grid(row=0, column=0)

btn_parentesis_fecha = Button(botoes, command = lambda: mostrar_num(')'), text=")", width=9, height=2, bg='orange')
btn_parentesis_fecha.grid(row=0, column=1)

btn_porcentagem = Button(botoes, command = lambda: mostrar_num('%'), text="%", width=9, height=2, bg='orange')
btn_porcentagem.grid(row=0, column=2)

btn_deletar = Button(botoes, command=limpar_tela, text="C", width=9, height=2, bg='orange')
btn_deletar.grid(row=0, column=3)

#LINHA 2
btn_7 = Button(botoes, command = lambda: mostrar_num('7'), text="7", width=9, height=2)
btn_7.grid(row=1, column=0)

btn_8 = Button(botoes, command = lambda: mostrar_num('8'), text="8", width=9, height=2)
btn_8.grid(row=1, column=1)

btn_9 = Button(botoes, command = lambda: mostrar_num('9'), text="9", width=9, height=2)
btn_9.grid(row=1, column=2)

btn_dividir = Button(botoes, command = lambda: mostrar_num('/'), text="/", width=9, height=2, bg='orange')
btn_dividir.grid(row=1, column=3)

#LINHA 3

btn_4 = Button(botoes, command = lambda: mostrar_num('4'), text="4", width=9, height=2)
btn_4.grid(row=2, column=0)

btn_5 = Button(botoes, command = lambda: mostrar_num('5'), text="5", width=9, height=2)
btn_5.grid(row=2, column=1)

btn_6 = Button(botoes, command = lambda: mostrar_num('6'), text="6", width=9, height=2)
btn_6.grid(row=2, column=2)

btn_multiplicar = Button(botoes, command = lambda: mostrar_num('*'), text="X", width=9, height=2, bg='orange')
btn_multiplicar.grid(row=2, column=3)

#LINHA 4
btn_1 = Button(botoes, command = lambda: mostrar_num('1'), text="1", width=9, height=2)
btn_1.grid(row=3, column=0)

btn_2 = Button(botoes, command = lambda: mostrar_num('2'), text="2", width=9, height=2)
btn_2.grid(row=3, column=1)

btn_3 = Button(botoes, command = lambda: mostrar_num('3'), text="3", width=9, height=2)
btn_3.grid(row=3, column=2)

btn_subtrair = Button(botoes, command = lambda: mostrar_num('-'), text="-", width=9, height=2, bg='orange')
btn_subtrair.grid(row=3, column=3)

#LINHA 5
btn_0 = Button(botoes, command = lambda: mostrar_num('0'), text="0", width=9, height=2)
btn_0.grid(row=4, column=0)

btn_ponto = Button(botoes, command = lambda: mostrar_num('.'), text=".", width=9, height=2, bg='orange')
btn_ponto.grid(row=4, column=1)

btn_resultado = Button(botoes, command = calcular, text="=", width=9, height=2, bg='orange')
btn_resultado.grid(row=4, column=2)

btn_somar= Button(botoes, command = lambda: mostrar_num('+'), text="+", width=9, height=2, bg='orange')
btn_somar.grid(row=4, column=3)

root.mainloop()
