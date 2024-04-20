# Credits to CodersLegacy -> https://coderslegacy.com/python/make-scrollable-frame-in-tkinter/

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
 
class VerticalScrolledFrame(ttk.Frame):
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)
 
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, 
                                width = 1000, height = 1000,
                                yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command = self.canvas.yview)
 
        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
 
        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = ttk.Frame(self.canvas)
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)

    def _on_mousewheel(self, event):
        if event.num == 5:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _configure_interior(self, event):
        # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width = self.interior.winfo_reqwidth())
         
    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())