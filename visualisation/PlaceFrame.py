from tkinter import Frame


class PlaceFrame(Frame):

    def notify(self, changed_values):
        for key, value in changed_values.items():
            if (key == 'starving') & value:
                self.configure(background='black')
