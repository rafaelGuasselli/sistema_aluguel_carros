import tkinter as Tk
from view.vertical_scrolled_frame import VerticalScrolledFrame

class Lista(VerticalScrolledFrame):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw)

