import tkinter
from random import randint
from pathlib import Path

class DiceSimulatorScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.root_path = Path(__file__).parent.parent

        self.dices = {
            0: '\\assets\\DicesNum\\Dice.png',
            1: '\\assets\\DicesNum\\DiceOne.png',
            2: '\\assets\\DicesNum\\DiceTwo.png',
            3: '\\assets\\DicesNum\\DiceThree.png',
            4: '\\assets\\DicesNum\\DiceFour.png',
            5: '\\assets\\DicesNum\\DiceFive.png',
            6: '\\assets\\DicesNum\\DiceSix.png'
        }

        self.dice_one = tkinter.StringVar()
        self.dice_two = tkinter.StringVar()

        self.dice_one.set(f'{self.root_path}{self.dices[0]}')
        self.dice_two.set(f'{self.root_path}{self.dices[0]}')

        self.dice_one_img = tkinter.PhotoImage(file=self.dice_one.get())
        self.dice_two_img = tkinter.PhotoImage(file=self.dice_two.get())


        self.create_widgets()

    def roll_dices(self):
        dice_num_one = randint(1, 6)
        dice_num_two = randint(1, 6)
        self.dice_one.set(f'{self.root_path}{self.dices[dice_num_one]}')
        self.dice_two.set(f'{self.root_path}{self.dices[dice_num_two]}')
        self.dice_one_img.configure(file=self.dice_one.get())
        self.dice_two_img.configure(file=self.dice_two.get())
        
    def back_menu(self):
        self.dice_one.set(f'{self.root_path}{self.dices[0]}')
        self.dice_two.set(f'{self.root_path}{self.dices[0]}')
        self.dice_one_img.configure(file=self.dice_one.get())
        self.dice_two_img.configure(file=self.dice_two.get())
        self.controller.show_frame('MenuGames')

    def create_widgets(self):
        tkinter.Label(self, text='Simulador de dados').grid(column=0, row=0)
        tkinter.Label(self, image=self.dice_one_img).grid(column=0, row=1)
        tkinter.Label(self, image=self.dice_two_img).grid(column=0, row=2)
        tkinter.Button(self, text='Tirar dados', command=self.roll_dices).grid(column=0, row=3)
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=4)
