"""Graphics module
PyXO game in graphic mode.
Run on a graphics window generated using TK"""

from tkinter import *
from .terminal import Grid
from tkinter import font


class GameWindow(Tk):
    """Game Window Class
    maintaining the game window 
    when in graphics mode

    Args:
        tk (tkinter.tk): TK root window class from which we inherit
    """
    def __init__(self, title="PyXO"):
        """Constructor for the GameWindow Class
        """
        super().__init__()
        self.config(bg='white')
        self.title(title)
        self.maxsize(width=520, height=545)
        self.minsize(width=520, height=545)
        self.resizable(None, None)
        self.__grid =  Grid().empty
        self.__buttons = Grid().empty
        self.__game_board__()
        self.__display_board__()
        
    def __game_board__(self):
        """ Creates the game board with the buttons """
        game_frame = Frame(master=self)
        game_frame.pack(fill=X)
        self.display = Label(master=game_frame, text='Testing', font=font.Font(size=28, weight="bold"))
        self.display.pack()
        return {}
    
    @property
    def buttons(self):
        return self.__buttons
    
    def __display_board__(self):
        grid_frame = Frame(master=self)
        grid_frame.pack()
        for i, row in enumerate(self.__grid):
            self.rowconfigure(i, weight=1, minsize=50)
            self.columnconfigure(i, weight=1, minsize=75)
            for j, col in enumerate(row):
                button = Button(master=grid_frame, font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=5,
                    height=2,
                    highlightbackground="blue")
                self.__buttons[i][j] = button
                button.grid(row=i,
                    column=j,
                    padx=5,
                    pady=5,
                    sticky="nsew")
        return {}


def main() -> int:
    root = GameWindow()
    root.mainloop()