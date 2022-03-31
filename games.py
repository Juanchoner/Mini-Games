import tkinter
from assets import styles
from pathlib import Path
import os

class MenuGames(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller

        self.root_path = Path(__file__).parent

        self.game_images = {
            0: os.path.join('assets', 'Menu', 'RockPaperScissors.png'),
            1: os.path.join('assets', 'Menu', 'GuessNumber.png'),
            2: os.path.join('assets', 'Menu', 'DiceSimulator.png')
        }

        self.rock_paper_scissors_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[0]))
        self.guess_number_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[1]))
        self.dice_simulator_img = tkinter.PhotoImage(file=os.path.join(self.root_path, self.game_images[2]))

        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self, text='Mini Games', **styles.TITLES).grid(column=0, row=0)
        tkinter.Button(self, image=self.rock_paper_scissors_img, command=lambda: self.controller.show_frame("RockPaperScissorsScreen")).grid(column=0, row=1)
        tkinter.Button(self, image=self.guess_number_img, command=lambda: self.controller.show_frame("GuessNumberScreen")).grid(column=0, row=2)
        tkinter.Button(self, image=self.dice_simulator_img, command=lambda: self.controller.show_frame("DiceSimulatorScreen")).grid(column=0, row=3)
        tkinter.Button(self, text='Hangman', command=lambda: self.controller.show_frame("HangmanScreen")).grid(column=0, row=4)

        self.grid_columnconfigure(0, weight=1)
