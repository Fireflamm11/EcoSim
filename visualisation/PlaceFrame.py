import tkinter as tk

"""
Refer:
https://stackoverflow.com/questions/26583602/displaying-data-in-a-hexagonal-grid-using-python
"""


class PlaceFrame(tk.Frame):

    def generate_children(self):
        tk.Label(self, name='pops', text=0, width=2, foreground='green').pack(
            fill=tk.BOTH)
        tk.Label(self, name='dead', text=0, width=2).pack(fill=tk.BOTH)

    def notify(self, changed_values):
        for key, value in changed_values.items():
            if (key == 'starving') & value:
                self.configure(background='black')
            if key == 'dead':
                label = self.nametowidget('dead')
                dead = int(label.cget('text')) + value
                label.configure(text=dead)
            if key == 'new_pops':
                label = self.nametowidget('pops')
                label.configure(text=value)
