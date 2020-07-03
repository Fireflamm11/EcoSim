import tkinter as tk

"""
Refer:
https://stackoverflow.com/questions/26583602/displaying-data-in-a-hexagonal-grid-using-python
"""


class PlaceFrame(tk.Frame):

    def generate_children(self):
        tk.Label(self, name='pops', text=0, width=4,
                 foreground='green').pack(fill=tk.BOTH)
        tk.Label(self, name='dead', text=0, width=4).pack(fill=tk.BOTH)
        tk.Label(self, name='migrants', text=0, width=4,
                 foreground='blue').pack(fill=tk.BOTH)

    def notify(self, changed_values):
        for key, value in changed_values.items():
            try:
                label = self.nametowidget(key)
                label.configure(text=value)
            except KeyError:
                if (key == 'starving') & value:
                    self.configure(background='black')
