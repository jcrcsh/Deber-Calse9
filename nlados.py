from Tkinter import *
import turtle

nLados= int(input("ingrese el numero de lados: "))

def graficarFigura():
    t=turtle.Pen()
	angulo = (180/lados)+180
	t.pencolor("red")
	for x in range(0,lados):
		t.forward(250)
		t.right(angulo)
	turtle.getscreen()._root.mainloop()

graficarFigura()