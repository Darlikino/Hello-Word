"""Нужно доделать норму с радиокнопками
сделать чтобы работало с одной кнопки
либо считало онлайн
"""

def probeg(event):
    #высчитывем пробег за месяц
    probeg1 = ent.get()
    probeg1 = int(probeg1)
    probeg2 = ent1.get()
    probeg2 = int(probeg2)
    lblmonth.configure(text = probeg1 - probeg2)

def litr(event):
    che1 = chek1.get()
    che1 = float(che1)
    che2 = chek2.get()
    che2 = float(che2)
    lblLitr.configure(text = che1 - che2)

def ostatok(event):
    #высчитываем остаток литров
    probeg1 = ent.get()
    probeg1 = int(probeg1)
    probeg2 = ent1.get()
    probeg2 = int(probeg2)
    ostprobeg = (probeg1 - probeg2) * 0.09
    che1 = chek1.get()
    che1 = float(che1)
    che2 = chek2.get()
    che2 = float(che2)
    ostchek = che1 - che2
    if ostprobeg > ostchek:
        ostlit.configure(text = "{0:.2f}".format( ostprobeg - ostchek), bg = 'lightgreen')
    else:
        ostlit.configure(text = "{0:.2f}".format( ostprobeg - ostchek), bg = 'red')



def clean(event):
    #очистка полей
    ent.delete(0, END)
    ent1.delete(0, END)
    chek1.delete(0, END)
    chek2.delete(0, END)
    entbak.delete(0, END)
    lblmonth.configure(text = " ")
    lblLitr.configure(text = " ")

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Расчет пробега")
root.geometry('580x580')


#наш светлозеленый фон
fra = Frame(root, width = 600, height = 200, bg = 'lightgreen', bd = 10)
itogi = Frame(root, width = 600, height = 200, bg = 'lightblue', bd = 10)
fra.pack()
itogi.pack()


#Метка пробега
lab  = Label(fra, text = "Пробег на спидометре ",
             font = "Arial 18", bg = 'lightgreen')
lab1 = Label(fra, text = "Пробег в путевке",
             font = "Arial 18", bg = 'lightyellow')
lab.grid(row = 1, column = 1, padx=20, pady=10)
lab1.grid(row = 1, column = 2, padx=20, pady=10)


#Метка чеков
labch  = Label(fra, text = "Последний чек ",
             font = "Arial 18", bg = 'lightgreen')
labch1 = Label(fra, text = "Первый чек",
             font = "Arial 18", bg = 'lightyellow')
labch.grid(row = 3, column = 1, padx=20)
labch1.grid(row = 3, column = 2, padx=20)


#Поля пробега
ent  = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#пробег на спидометре
ent.grid(row = 2, column = 1, padx=20)
ent1 = Entry(fra, width = 15, bd = 2,
             font="Arial 18", bg = 'yellow')#пробег по путевке
ent1.grid(row = 2, column = 2, padx=20)


#Поля чеков
chek1  = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#последний чек
chek1.grid(row = 4, column = 1, padx=20)
chek2 = Entry(fra, width = 15, bd = 2,
             font="Arial 18", bg = 'yellow')#первый чек
chek2.grid(row = 4, column = 2, padx=20)


#Метка и поле Остаток в баке
labbak = Label(fra, text ="Остаток в баке ",
               font ="Arial 18", bg = 'lightgreen')
labbak.grid(row = 5, column = 1, padx = 20)
entbak = Entry(fra, width = 15, bd = 2,
               font ='Arial 18')
entbak.grid(row = 6, column = 1, padx = 20)


#Норма расхода
labnor = Label(fra, text ="Норма",
               font ="Arial 18", bg = 'lightgreen')
labnor.grid(row = 5, column = 2, padx = 20)
var = IntVar()
var.set(0)
rad0 = Radiobutton(fra, text ='9.0')
rad1 = Radiobutton(fra, text ='9.2')
rad0.grid(row=6, column = 2, padx = 20)
rad1.grid(row=6, column = 3, padx = 20)


#метка и поле пробега за месяц
lab21 = Label(itogi, text=' Пробег за месяц: ',
              font='Arial 18', bg='darkgrey')
lab21.grid(row = 1, column = 1, padx = 49, pady = 10)
lblmonth = Label(itogi, width = 13, bd = 2,
              text = ' ', font='Arial 18', bg = 'darkgrey')
lblmonth.grid(row=1, column = 2, padx=30, pady = 10)


#метка и поле литров за МЕСЯЦ
labch21 = Label(itogi, text=' Литров за месяц: ',
              font='Arial 18', bg='darkgrey')
labch21.grid(row = 2, column = 1, padx = 49, pady = 10)
lblLitr = Label(itogi, width = 13, bd = 2,
               font='Arial 18', bg = 'darkgrey')
lblLitr.grid(row=2, column = 2, padx=30, pady = 10)


#Метка и поле Остаток литров
lablit = Label(itogi, text ="Остаток литров: ",
               font ="Arial 18", bg = 'darkgrey')
lablit.grid(row = 3, column = 1, padx = 49, pady = 10)
ostlit = Label(itogi, width = 13, bd = 2,
               text = ' ', font ='Arial 18', bg = 'darkgrey')
ostlit.grid(row = 3, column = 2, padx = 30, pady = 10)


#кнопка расчета
but = ttk.Button(root, text='Расчитать')
but.pack()
but.bind("<Button-1>", probeg)
but.bind("<Button-3>", litr)
but.bind("<Button-2>", ostatok)

#кнопка отчистки
but1 = Button(root, text='очистить', font ='Arial 18', bd = 2)
but1.pack()
but1.bind("<Button-1>", clean)



lbl = Label(root, text = 'text')
lbl.pack()
root.mainloop()


