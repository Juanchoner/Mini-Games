import tkinter
from assets import styles
from games import MenuGames
from RockPaperScissors.RockPaperScissors import RockPaperScissorsScreen
from GuessNumber.GuessNumber import GuessNumberScreen
from Dices.DiceSimulator import DiceSimulatorScreen

class Manager(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Mini games')
        container = tkinter.Frame(self)
        container.pack(
            side = tkinter.TOP,
            fill = tkinter.BOTH,
            expand = True
        )
        container.configure(background = styles.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for screen in (MenuGames, RockPaperScissorsScreen, GuessNumberScreen, DiceSimulatorScreen):
            name_screen = screen.__name__
            frame = screen(container, self)
            self.frames[name_screen] = frame
            frame.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.show_frame("MenuGames")

    def show_frame(self, container: str):
        frame = self.frames[container]
        frame.tkraise()
