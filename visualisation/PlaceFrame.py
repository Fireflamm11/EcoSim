from tkinter import Frame

"""
Refer:
https://stackoverflow.com/questions/26583602/displaying-data-in-a-hexagonal-grid-using-python
"""


class PlaceFrame(Frame):

    def notify(self, changed_values):
        for key, value in changed_values.items():
            if (key == 'starving') & value:
                self.configure(background='black')
