import tkinter as tk
from tkinter import messagebox
from Game_Logic import win, draw, ai_move


BG_COLOR = "#121212"
CARD_COLOR = "#1E1E1E"
BTN_COLOR = "#2C2C2C"
BTN_HOVER = "#3A3A3A"
TEXT_COLOR = "#FFFFFF"
ACCENT_COLOR = "#00ADB5"


class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic-Tac-Toe")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self.center_window(800, 600)

        self.game_mode = None          
        self.player_symbol = None
        self.ai_symbol = None
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Screen in (
            WelcomeScreen,
            ModeSelectionScreen,
            SymbolSelectionScreen,
            GameScreen
        ):
            frame = Screen(self.container, self)
            self.frames[Screen.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeScreen")

    def center_window(self, width, height):
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def show_frame(self, name):
        frame = self.frames[name]

        if name == "GameScreen":
            self.board = [" " for _ in range(9)]
            if self.game_mode == "AI":
                self.current_player = self.player_symbol
            else:
                self.current_player = "X"
            frame.reset_board()

        frame.tkraise()


class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)

        center = tk.Frame(self, bg=BG_COLOR)
        center.pack(expand=True)

        tk.Label(
            center,
            text="Welcome to Tic-Tac-Toe",
            font=("Arial", 26),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=1)
        
        tk.Label(
            center,
            text="A Program by Saurabh Jha",
            font=("Arial", 16),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=1)

        tk.Button(
            center,
            text="Start Game",
            width=16,
            height=2,
            font=("Arial", 12),
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=BTN_HOVER,
            bd=0,
            command=lambda: controller.show_frame("ModeSelectionScreen")
        ).pack(pady=30)


class ModeSelectionScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)

        center = tk.Frame(self, bg=BG_COLOR)
        center.pack(expand=True)

        tk.Label(
            center,
            text="Choose Game Mode",
            font=("Arial", 22),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=30)

        tk.Button(
            center,
            text="Player vs AI",
            width=16,
            height=2,
            font=("Arial", 12),
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=BTN_HOVER,
            bd=0,
            command=lambda: self.select_mode(controller, "AI")
        ).pack(pady=10)

        tk.Button(
            center,
            text="Player vs Player",
            width=16,
            height=2,
            font=("Arial", 12),
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=BTN_HOVER,
            bd=0,
            command=lambda: self.select_mode(controller, "PVP")
        ).pack(pady=10)

    def select_mode(self, controller, mode):
        controller.game_mode = mode
        if mode == "AI":
            controller.show_frame("SymbolSelectionScreen")
        else:
            controller.player_symbol = None
            controller.ai_symbol = None
            controller.show_frame("GameScreen")


class SymbolSelectionScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)

        center = tk.Frame(self, bg=BG_COLOR)
        center.pack(expand=True)

        tk.Label(
            center,
            text="Choose Your Symbol",
            font=("Arial", 22),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=30)

        tk.Button(
            center,
            text="Play as X",
            width=16,
            height=2,
            font=("Arial", 12),
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=BTN_HOVER,
            bd=0,
            command=lambda: self.select_symbol(controller, "X")
        ).pack(pady=10)

        tk.Button(
            center,
            text="Play as O",
            width=16,
            height=2,
            font=("Arial", 12),
            bg=BTN_COLOR,
            fg=TEXT_COLOR,
            activebackground=BTN_HOVER,
            bd=0,
            command=lambda: self.select_symbol(controller, "O")
        ).pack(pady=10)

    def select_symbol(self, controller, symbol):
        controller.player_symbol = symbol
        controller.ai_symbol = "O" if symbol == "X" else "X"
        controller.show_frame("GameScreen")


class GameScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)

        self.controller = controller
        self.buttons = []

        center = tk.Frame(self, bg=BG_COLOR)
        center.pack(expand=True)

        self.status = tk.Label(
            center,
            text="",
            font=("Arial", 16),
            bg=BG_COLOR,
            fg=ACCENT_COLOR
        )
        self.status.pack(pady=20)

        board_frame = tk.Frame(center, bg=BG_COLOR)
        board_frame.pack()

        for i in range(9):
            btn = tk.Button(
                board_frame,
                text=" ",
                font=("Arial", 28),
                width=4,
                height=2,
                bg=CARD_COLOR,
                fg=TEXT_COLOR,
                activebackground=ACCENT_COLOR,
                bd=0,
                command=lambda i=i: self.make_move(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=6, pady=6)
            self.buttons.append(btn)

    def reset_board(self):
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.update_status()

    def update_status(self):
        self.status.config(text=f"Turn: {self.controller.current_player}")

    def make_move(self, index):
        if self.controller.board[index] != " ":
            return

        current = self.controller.current_player
        self.place_move(index, current)

        if self.check_game_end(current):
            return

        if self.controller.game_mode == "AI":
            ai = self.controller.ai_symbol
            human = self.controller.player_symbol

            ai_index = ai_move(self.controller.board, ai, human)
            if ai_index is not None:
                self.place_move(ai_index, ai)
                if self.check_game_end(ai):
                    return

            self.controller.current_player = human
        else:
            self.controller.current_player = "O" if current == "X" else "X"

        self.update_status()

    def place_move(self, index, player):
        self.controller.board[index] = player
        self.buttons[index].config(text=player, state="disabled")

    def check_game_end(self, player):
        if win(self.controller.board, player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            self.controller.show_frame("WelcomeScreen")
            return True

        if draw(self.controller.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.controller.show_frame("WelcomeScreen")
            return True

        return False



if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()
