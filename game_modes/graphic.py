"""Graphics module
PyXO game in graphic mode.
Run on a graphics window generated using TK"""

from functools import partial
from tkinter import *
from .terminal import Grid
from tkinter import font
import sys, random

class GameWindow(Tk):
    """Game Window Class
    maintaining the game window 
    when in graphics mode

    Args:
        tk (tkinter.tk): TK root window class from which we inherit
    """
    __turn = random.choice([True, False])
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
        self.__player1 = Player('X', 'blue')
        self.__player2 = Player('O', 'red')
        self.__players = {True: self.__player1, False: self.__player2}
        self.__game_state = f'Player {self.__players[GameWindow.__turn].label} Ready?'
        self.__create_menu()
        self.__game_board__()
        self.__display_board__()  

    def __game_board__(self):
        """ Creates the game board with the buttons """
        game_frame = Frame(master=self)
        game_frame.pack(fill=X)
        self.display = Label(master=game_frame, text=f"{self.__game_state}", font=font.Font(size=28, weight="bold"))
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
                    highlightbackground="blue",)
                button.bind("<Button-1>", self.play)
                self.__buttons[i][j] = button
                button.grid(row=i,
                    column=j,
                    padx=5,
                    pady=5,
                    sticky="nsew")
        return {}

    def play(self, event):
        self.display.config(text=f"{self.__game_state}'s Turn")
        winner = self.winner()
        if winner:
            self.display.config(text=winner)
            return
        
        game_over = self.game_over()
        if game_over:
            self.display.config(text='Game Over, No Winner!!!')
            return 
        
        if event.widget.cget('text'):
            return

        event.widget.config(text=self.__players[GameWindow.__turn].label, fg=self.__players[GameWindow.__turn].color)
        self.__grid[event.widget.grid_info()['row']][event.widget.grid_info()['column']] = self.__players[GameWindow.__turn].label

        winner = self.winner()
        if winner:
            self.display.config(text=winner)
            return
        
        game_over = self.game_over()
        if game_over:
            self.display.config(text='Game Over, No Winner!!!')
            return
        
        GameWindow.__turn ^= True
        self.__game_state = f'{self.__players[GameWindow.__turn].label}'
        self.display.config(text=f"{self.__game_state}'s Turn")
    
    def winner(self):
        winner = None
        # Row Win
        if self.__grid[0][0] and self.__grid[0][0] == self.__grid[0][1] and self.__grid[0][1] == self.__grid[0][2]:
            return f"Winner is Player {self.__grid[0][0]}"
        if self.__grid[1][0] and self.__grid[1][0] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[1][2]:
            return f"Winner is Player {self.__grid[1][0]}"
        if self.__grid[2][0] and self.__grid[2][0] == self.__grid[2][1] and self.__grid[2][1] == self.__grid[2][2]:
            return f"Winner is Player {self.__grid[2][0]}"
        
        # Column Win
        if self.__grid[0][0] and self.__grid[0][0] == self.__grid[1][0] and self.__grid[1][0] == self.__grid[2][0]:
            return f"Winner is Player {self.__grid[0][0]}"
        if self.__grid[0][1] and self.__grid[0][1] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[2][1]:
            return f"Winner is Player {self.__grid[0][1]}"
        if self.__grid[0][2] and self.__grid[0][2] == self.__grid[1][2] and self.__grid[1][2] == self.__grid[2][2]:
            return f"Winner is Player {self.__grid[0][2]}"
        
        # Diagonal Win
        if self.__grid[0][0] and self.__grid[0][0] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[2][2]:
            return f"Winner is Player {self.__grid[0][0]}"
        if self.__grid[0][2] and self.__grid[0][2] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[2][0]:
            return f"Winner is Player {self.__grid[0][2]}"
        return winner
    
    def game_over(self):
        self.__grid
        res = list(map(lambda x: list(filter(lambda y: True if y == 'X' or y == 'O' else False , x)), self.__grid))
        return len(res[0]) == 3 and len(res[1]) == 3 and len(res[2]) == 3
    
    def __create_menu(self):
        menu_bar = Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = Menu(master=menu_bar)
        file_menu.add_command(
            label="Play Again",
            command=self.reset
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=partial(quit, 'Game ended without issues'))
        menu_bar.add_cascade(label="File", menu=file_menu)

    def reset(self):
        self.__grid = list(Grid().empty)
        for buttons in self.__buttons:
            for button in buttons:
                button.config(text='')
        self.display.config(text=f'Player {self.__players[GameWindow.__turn].label} Ready?')

class Player:
    """Player Class
    """
    def __init__(self, label, color):
        self.__color = color
        self.__label = label
    
    @property
    def color(self):
        return self.__color
    
    @property
    def label(self):
        return str(self.__label)


def main() -> int:
    try:
        root = GameWindow()
        root.mainloop()
    except BaseException as e:
        print(e)
    finally:
        return 1
