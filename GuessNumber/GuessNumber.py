import tkinter
from assets import styles
import random

class GuessNumberScreen(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = styles.BACKGROUND)
        self.controller = controller

        self.user_selection = tkinter.IntVar()
        self.show_machine_selection = tkinter.IntVar()

        self.user_message = tkinter.StringVar()
        self.machine_message = tkinter.StringVar()

        self.win_message = tkinter.StringVar()

        self.num_min = 0
        self.num_max = 100

        self.tem_min = 0
        self.tem_max = 100

        self.guess_number = random.randint(self.num_min, self.num_max)

        self.user_selection.set('')
        self.show_machine_selection.set('')
        self.creat_widgets()

    def number_machine(self):
        number = random.randint(self.num_min, self.num_max)
        self.show_machine_selection.set(number)
        return number

    def closest_number(self, num: int):
        if num < self.guess_number:
            tem = self.guess_number - num
            if num > self.tem_min:
                self.num_min = num
                self.tem_min = num
        else:
            tem = num - self.guess_number
            if num < self.tem_max:
                self.num_max = num
                self.tem_max = num

    def reset_values(self):
        self.num_min = 0
        self.num_max = 100
        self.tem_min = 0
        self.tem_max = 100
        self.guess_number = random.randint(self.num_min, self.num_max)

    def message(self, number: int):
        if self.guess_number == number:
            self.reset_values()
            return 'Has ganado!!!'
        elif self.guess_number < number:
            self.closest_number(number)
            return f'El número es menor a {number}'
        else:
            self.closest_number(number)
            return f'El número es mayor a {number}'

    def message_info(self, number_selected: int, player: str):
        if player == "usuario":
            self.user_message.set(self.message(number_selected))
        else:
            self.machine_message.set(self.message(number_selected))

    def start_game(self):
        number_user = self.user_selection.get()
        self.message_info(number_user, "usuario")
        number_machine = self.number_machine()
        self.message_info(number_machine, 'máquina')

    def back_menu(self):
        self.reset_values()
        self.user_selection.set('')
        self.user_message.set('')
        self.show_machine_selection.set('')
        self.machine_message.set('')
        self.controller.show_frame('MenuGames')

    def creat_widgets(self):
        tkinter.Label(self, text='Adivina el número del 0 al 100').grid(column=0, row=0, sticky=tkinter.NSEW)
        tkinter.Entry(self, textvariable=self.user_selection).grid(column=0, row=1, sticky=tkinter.NSEW)
        tkinter.Button(self, text='Seleccionar', command=self.start_game).grid(column=0, row=2, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.user_message).grid(column=0, row=3, sticky = tkinter.NSEW)
        tkinter.Label(self, text='La máquina a seleccionado:').grid(column=0, row=4, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.show_machine_selection).grid(column=0, row=5, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.machine_message).grid(column=0, row=6, sticky = tkinter.NSEW)
        tkinter.Label(self, textvariable=self.win_message).grid(column=0, row=7, sticky = tkinter.NSEW)
        tkinter.Button(self, text='⏮', command=self.back_menu).grid(column=0, row=8, sticky=tkinter.NSEW)
