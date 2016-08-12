__author__ = 'Alex'
import tkinter

def paint(event):
    #обработчик событий холста
    print(event.x, event.y)
    if event.widget != canvas:
        print("Странно")
        return
    canvas.coords(line, 0, 0, event.x, event.y)

root = tkinter.Tk()

canvas = tkinter.Canvas(root, background ='white', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    oval = canvas.create_oval(i*40, i*40, i*40+30, i*40+30, width=2, fill='green')

root.mainloop()
print("эта строка будет достигнута при выходе из приложения")