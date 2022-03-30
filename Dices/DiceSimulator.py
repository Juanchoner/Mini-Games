import tkinter
from assets import styles
from random import randint
from pathlib import Path
import os

class DiceSimulatorScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.controller = controller
        
        self.root_path = Path(__file__).parent.parent

        self.dices = {
            0: os.path.join('assets', 'DicesNum', 'Dice.png'),
            1: os.path.join('assets', 'DicesNum', 'DiceOne.png'),
            2: os.path.join('assets', 'DicesNum', 'DiceTwo.png'),
            3: os.path.join('assets', 'DicesNum', 'DiceThree.png'),
            4: os.path.join('assets', 'DicesNum', 'DiceFour.png'),
            5: os.path.join('assets', 'DicesNum', 'DiceFive.png'),
            6: os.path.join('assets', 'DicesNum', 'DiceSix.png')
        }

        self.dice_one = tkinter.StringVar()
        self.dice_two = tkinter.StringVar()

        self.dice_one.set(os.path.join(self.root_path, self.dices[0]))
        self.dice_two.set(os.path.join(self.root_path, self.dices[0]))

        self.dice_one_img = tkinter.PhotoImage(file=self.dice_one.get())
        self.dice_two_img = tkinter.PhotoImage(file=self.dice_two.get())


        self.create_widgets()

    def roll_dices(self):
        dice_num_one = randint(1, 6)
        dice_num_two = randint(1, 6)
        self.dice_one.set(os.path.join(self.root_path, self.dices[dice_num_one]))
        self.dice_two.set(os.path.join(self.root_path, self.dices[dice_num_two]))
        self.dice_one_img.configure(file=self.dice_one.get())
        self.dice_two_img.configure(file=self.dice_two.get())
        
    def back_menu(self):
        self.dice_one.set(os.path.join(self.root_path, self.dices[0]))
        self.dice_two.set(os.path.join(self.root_path, self.dices[0]))
        self.dice_one_img.configure(file=self.dice_one.get())
        self.dice_two_img.configure(file=self.dice_two.get())
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Simulador de dados', **styles.TITLES).grid(column=0, row=0)
        tkinter.Label(self, image=self.dice_one_img).grid(column=0, row=1)
        tkinter.Label(self, image=self.dice_two_img).grid(column=0, row=2)
        tkinter.Button(self, text='Tirar dados', command=self.roll_dices).grid(column=0, row=3)
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=4, sticky=tkinter.NSEW)

        self.grid_columnconfigure(0, weight=1)
