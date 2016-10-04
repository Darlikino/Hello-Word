"""Нужно доделать норму с радиокнопками
сделать чтобы работало с одной кнопки
либо считало онлайн
"""
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
"""
def ostatok(event):
    #высчитываем остаток литров
    if normal.get() == 1:
        norma = 0.092
    else:
        norma = 0.09
    print(norma)

    probeg1 = ent.get()
    probeg1 = int(probeg1)
    probeg2 = ent1.get()
    probeg2 = int(probeg2)
    lblmonth.configure(text = probeg1 - probeg2)

    ostprobeg = (probeg1 - probeg2) * norma
    che1 = chek1.get()
    che1 = float(che1)
    che2 = chek2.get()
    che2 = float(che2)
    lblLitr.configure(text = che1 - che2)

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
    ostlit.configure(text = " ")

#функция меню. закрывает программу
def close_app():
    root.destroy()

#функция меню. Помощь
def help_app():
    pass

#функция меню. О программе
def about_app():
    win = Toplevel(root)
    win.geometry('250x150')
    win.title("О программе")
    lab = Label(win, text = "Программа подсчета остатка бензина \n Версия 1.0")
    lab.pack()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Расчет пробега")
root.geometry('580x580')


#Создаем меню
menu = Menu(root)
root.config(menu = menu)
fm = Menu(menu)
menu.add_cascade(label = 'File', menu = fm)
fm.add_command(label = 'Exit', command = close_app)

sm = Menu(menu)
menu.add_cascade(label = 'Help', menu = sm)
sm.add_command(label = 'Help', command = help_app)
sm.add_command(label = 'About', command = about_app)


#наш фон
fra = Frame(root, width = 600, height = 200, bg = 'Cornsilk1', bd = 10)
itogi = Frame(root, width = 600, height = 200, bg = 'Cornsilk1', bd = 10)
fra.pack()
itogi.pack()


#Метка пробега
lab  = Label(fra, text = "Пробег на спидометре ",
             font = "Arial 18", bg = 'Cornsilk1')
lab1 = Label(fra, text = "Пробег в путевке",
             font = "Arial 18", bg = 'Cornsilk1')
lab.grid(row = 1, column = 1, padx=20, pady=10)
lab1.grid(row = 1, column = 2, padx=20, pady=10)


#Метка чеков
labch  = Label(fra, text = "Последний чек ",
             font = "Arial 18", bg = 'Cornsilk1')
labch1 = Label(fra, text = "Первый чек",
             font = "Arial 18", bg = 'Cornsilk1')
labch.grid(row = 3, column = 1, padx=20)
labch1.grid(row = 3, column = 2, padx=20)


#Поля пробега
ent  = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#пробег на спидометре
ent.grid(row = 2, column = 1, padx=20)
ent1 = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#пробег по путевке
ent1.grid(row = 2, column = 2, padx=20)


#Поля чеков
chek1  = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#последний чек
chek1.grid(row = 4, column = 1, padx=20)
chek2 = Entry(fra, width = 15, bd = 2,
             font="Arial 18")#первый чек
chek2.grid(row = 4, column = 2, padx=20)


#Метка и поле Остаток в баке
labbak = Label(fra, text ="Остаток в баке ",
               font ="Arial 18", bg = 'Cornsilk1')
labbak.grid(row = 5, column = 1, padx = 20)
entbak = Entry(fra, width = 15, bd = 2,
               font ='Arial 18')
entbak.grid(row = 6, column = 1, padx = 20)


#Норма расхода
labnor = Label(fra, text ="Норма",
               font ="Arial 18", bg = 'Cornsilk1')
labnor.grid(row = 5, column = 2, padx = 20)
normal = IntVar()
normal.set(0)
rad0 = Radiobutton(fra, text ='9.0', variable = normal, value = 0, bg = 'Cornsilk1')
rad1 = Radiobutton(fra, text ='9.2', variable = normal, value = 1, bg = 'Cornsilk1')
rad0.place(x = 355, y = 190)
rad1.place(x = 465, y = 190)


#метка и поле пробега за месяц
lab21 = Label(itogi, text=' Пробег за месяц: ',
              font='Arial 18', bg='Cornsilk1')
lab21.grid(row = 1, column = 1, padx = 49, pady = 10)
lblmonth = Label(itogi, width = 13, bd = 2,
              text = ' ', font='Arial 18', bg = 'Cornsilk1')
lblmonth.grid(row=1, column = 2, padx=30, pady = 10)


#метка и поле литров за МЕСЯЦ
labch21 = Label(itogi, text=' Литров за месяц: ',
              font='Arial 18', bg = 'Cornsilk1')
labch21.grid(row = 2, column = 1, padx = 49, pady = 10)
lblLitr = Label(itogi, width = 13, bd = 2,
               font='Arial 18', bg = 'Cornsilk1')
lblLitr.grid(row=2, column = 2, padx=30, pady = 10)


#Метка и поле Остаток литров
lablit = Label(itogi, text ="Остаток литров: ",
               font ="Arial 18", bg = 'Cornsilk1')
lablit.grid(row = 3, column = 1, padx = 49, pady = 10)
ostlit = Label(itogi, width = 13, bd = 2,
               text = ' ', font ='Arial 18', bg = 'Cornsilk1')
ostlit.grid(row = 3, column = 2, padx = 30, pady = 10)


#кнопка расчета
but = ttk.Button(root, text='Расчитать')
but.pack()
#but.bind("<Button-1>", probeg)
#but.bind("<Button-3>", litr)
but.bind("<Button-1>", ostatok)

#кнопка отчистки
but1 = Button(root, text='очистить', font ='Arial 18', bd = 2)
but1.pack()
but1.bind("<Button-1>", clean)



lbl = Label(root, text = 'остаток в баке пока не считает')
lbl.pack()
root.mainloop()


