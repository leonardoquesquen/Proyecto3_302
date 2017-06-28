from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
	anchoPincel = 1.0
	DEFAULT_COLOR = 'black'

	def __init__(self):
		self.ventana = Tk()
		self.ventana.title("Proyecto de Introducción a la ciencia de la computación")

		self.normal = Button(self.ventana, text='Normal', command=self.usoNormal)
		self.normal.grid(row=0, column=0)

		self.redondo = Button(self.ventana, text='Redondo', command=self.usoRedondo)
		self.redondo.grid(row=0, column=1)

		self.cuadrado = Button(self.ventana, text='Cuadrado', command=self.usoCuadrado)
		self.cuadrado.grid(row=0, column=2)

		self.colorSeleccion = Button(self.ventana, text='Color', command=self.eligeColor)
		self.colorSeleccion.grid(row=0, column=3)

		self.borrar = Button(self.ventana, text='Borrar', command=self.borrador)
		self.borrar.grid(row=0, column=4)

		self.tamanoBoton = Scale(self.ventana, from_=1, to=50, orient=HORIZONTAL)
		self.tamanoBoton.grid(row=1, column=2)

		self.areaDibujo = Canvas(self.ventana, bg='white', width=600, height=600)
		self.areaDibujo.grid(row=2, columnspan=5)

		self.old_x = None
		self.old_y = None
		self.ancho = self.tamanoBoton.get()
		self.color = self.DEFAULT_COLOR
		self.eraser_on = False
		self.botonActivo = self.normal
		self.botonActivo.config(relief=SUNKEN)
		self.areaDibujo.bind('<B1-Motion>', self.paint)
		self.tipo="normal"
		self.ventana.mainloop()



	def usoNormal(self):
		self.tipo="normal"
		self.activarBoton(self.normal)

	def usoRedondo(self):
		self.tipo="redondo"
		self.activarBoton(self.redondo)

	def usoCuadrado(self):
		self.tipo="cuadrado"
		self.activarBoton(self.cuadrado)

	def eligeColor(self):
		self.color = askcolor(color=self.color)[1]

	def borrador(self):
		self.tipo = "borrar"
		self.activarBoton(self.borrar , eraser_mode=True)

	def activarBoton(self, boton, eraser_mode=False):
		self.botonActivo.config(relief=RAISED)
		boton.config(relief=SUNKEN)
		self.botonActivo = boton
		self.eraser_on = eraser_mode

	def paint(self, event):
		self.ancho = self.tamanoBoton.get()
		colorPintar = 'white' if self.eraser_on else self.color
		x=event.x
		y=event.y

		if self.old_x and self.old_y:
			if self.tipo=="normal":
				self.areaDibujo.create_line(self.old_x, self.old_y, x, y,
						   width=self.ancho, fill=colorPintar,
						   capstyle=ROUND, smooth=TRUE, splinesteps=36)

			elif self.tipo=="redondo":
				r= self.ancho
				self.areaDibujo.create_oval(x-r, y-r, x+r,y+r,outline=colorPintar , fill=colorPintar)
			elif self.tipo=="cuadrado":
				self.areaDibujo.create_rectangle(x, y,x+self.ancho , y+self.ancho, outline=colorPintar, fill=colorPintar, width=2)
			else:
				self.areaDibujo.create_line(self.old_x, self.old_y, x, y, width=self.ancho, fill=colorPintar, capstyle=ROUND, smooth=TRUE, splinesteps=36)
		self.old_x = x
		self.old_y = y

if __name__ == '__main__':
	Paint()
