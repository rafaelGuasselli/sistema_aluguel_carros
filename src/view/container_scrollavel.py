import tkinter as tk
from tkinter.constants import *

class ContainerScrollavel(tk.Frame):
	def __init__(self, parent, *args, **kw):
		tk.Frame.__init__(self, parent, *args, **kw)
		self.inicializar(parent, *args, **kw)

	def inicializar(self, parent):
		self.parent = parent

		self.scrollbar = tk.Scrollbar(self, orient=VERTICAL)
		self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, height=1000, yscrollcommand=self.scrollbar.set)
		self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
		self.scrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
		self.scrollbar.config()

		self.canvas.xview_moveto(0)
		self.canvas.yview_moveto(0)

		self.container = tk.Frame(self.canvas)
		self.container_id = self.canvas.create_window(0, 0, window=self.container, anchor=NW)
		
		self.container.bind('<Configure>', self.__containerRedimencionado)
		self.canvas.bind('<Configure>', self.__canvasRedimencionado)

		self.parent.bind("<MouseWheel>", self.__onMouseScroll)
		self.parent.bind("<Button-4>", self.__onMouseScroll)
		self.parent.bind("<Button-5>", self.__onMouseScroll)

	def __onMouseScroll(self, event):
		containerHeight = self.container.winfo_reqheight()

		if containerHeight < self.scrollbar.winfo_height():
			return

		if event.num == 5:
			self.canvas.yview_scroll(1, "units")
		elif event.num == 4:
			self.canvas.yview_scroll(-1, "units")
		else:
			self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

	def __containerRedimencionado(self, event):
		containerWidth, containerHeight = (self.container.winfo_reqwidth(), self.container.winfo_reqheight())
		canvasWidth, canvasHeight = (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())
		
		self.canvas.config(scrollregion=(0, 0, containerWidth, containerHeight))
		if containerWidth != canvasWidth:
			self.canvas.config(width=containerWidth)

	def __canvasRedimencionado(self, event):
		containerWidth, containerHeight = (self.container.winfo_reqwidth(), self.container.winfo_reqheight())
		canvasWidth, canvasHeight = (self.canvas.winfo_width(), self.canvas.winfo_reqheight())

		if containerWidth != canvasWidth:
			self.canvas.itemconfigure(self.container_id, width=canvasWidth)