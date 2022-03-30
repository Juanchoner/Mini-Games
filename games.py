import tkinter

class MenuGames(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self, text='Games :)').grid(column=0, row=0)
        tkinter.Button(self, text='Piedra papel y tijera', command=lambda: self.controller.show_frame("RockPaperScissorsScreen")).grid(column=0, row=1)
        tkinter.Button(self, text='Adivina el número', command=lambda: self.controller.show_frame("GuessNumberScreen")).grid(column=0, row=2)
        tkinter.Button(self, text='Simulador de dados', command=lambda: self.controller.show_frame("DiceSimulatorScreen")).grid(column=0, row=3)
