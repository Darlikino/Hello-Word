__author__ = 'Alex'
import tkinter

def button1_command():
    print("button 11 default command.")
def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)

    me = event.widget

    if me == button1:
        print("hello")
    elif me == button2:
        print("you pressed button2")
    else:
        raise ValueError()

def init_main_window():

    #Инмциализация главного окна. Создание виджетов

    global root, button1, button2, label, text, suler
    root = tkinter.Tk()

    button1 = tkinter.Button(root, text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)
    button1.pack()

    button2 = tkinter.Button(root, text="Button 2")
    button2.bind("<Button>", print_hello)
    button2.pack()

    variable = tkinter.IntVar(0)
    label = tkinter.Label(textvariable=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length = 300,
                          from_=0, to = 100, tickinterval = 10, resolution = 5, variable = variable)
    text = tkinter.Entry(root, textvariable = variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()


if __name__ == "_main_":
    init_main_window()
    root.mainloop()
