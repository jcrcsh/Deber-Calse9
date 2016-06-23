from Tkinter import *

app=Tk()
canvas = Canvas (app, width=1000, height=1000)
canvas.pack()
canvas.create_polygon(490,280, 490,240,470,240, 500,200, 530,240, 510,240, 510,280)

def moverPoligonos(event):
	if event.keysym == 'Up':
		canvas.move(1, 0, -5)
	elif event.keysym == 'Down' :
		canvas.move(2, 0, 5)
	elif event.keysym == 'Left':
		canvas.move(4, -5, 0)
	else:
		canvas.move(3, 5,0)
		
canvas.bind_all('<KeyPress-Up>', moverPoligonos)
canvas.bind_all('<KeyPress-Down>', moverPoligonos)
canvas.bind_all('<KeyPress-Left>', moverPoligonos)
canvas.bind_all('<KeyPress-Right>', moverPoligonos)
app.mainloop()