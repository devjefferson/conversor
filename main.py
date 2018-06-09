from tkinter import *

#Janela
janela = Tk()
janela.geometry("280x300+200+200")
janela.title('Conversor de moedas')
janela.wm_iconbitmap('icone.ico')

def Comand_bt():
    lbbtctext['text'] =float(lbarea.get())/ 29940.84
    lbdogetext['text'] =float(lbarea.get())/ 0.01454
    lbusdtext['text'] =float(lbarea.get())*0.256
    lbeurotext['text'] =float(lbarea.get())*0.217

#Entry
lbarea = Entry(janela, width=20 ,text='')

#Botões

#bt2 = Button(janela, width=10, text="Limpar")
bt1 = Button(janela, width=10, text="Conversor", command=Comand_bt)
#Label e texto
lbreal = Label(janela, text='Real: ')
lbbtc = Label(janela, text='Bitcoin:')
lbdoge = Label(janela, text='Dogecoin:')
lbusd = Label(janela, text='Dollar:')
lbeuro = Label(janela, text='Euro:')

lbbtctext = Label(janela, text='')
lbdogetext = Label(janela, text='')
lbusdtext = Label(janela, text='')
lbeurotext = Label(janela, text='')

by = Label(janela, text='ByJeffersonFonseca')

#Posições
lbarea.place(x=60, y=70)
bt1.place(x=190, y=68)
#bt2.place(x=180, y=150)
lbreal.place(x=20, y=70)
lbusd.place(x=20, y=130)
lbeuro.place(x=20, y=160)
lbbtc.place(x=20, y=190)
lbdoge.place(x=20, y=220)
by.place(x=160, y=280)

lbusdtext.place(x=120, y=130)
lbeurotext.place(x=120, y=160)
lbbtctext.place(x=120, y=190)
lbdogetext.place(x=120, y=220)

janela.mainloop()

