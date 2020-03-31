from tkinter import Label, Tk, Button, Entry, Frame, messagebox
import socket
import threading
import json


IP = "0.0.0.0"
PORT = 69420


class Client:
    def __init__(self, host: bool, game: game):
        self.host = host
        self.parent_game = game
        self.c = None

    def start(self):
        pass

    def handle_data(self, data):
        if 'move':
            # if there is move data, place update the board
            self.parent_game.board[data['move']['y']][data['move']['x']] = self.parent_game.on_turn
        if 'onturn' in data:
            # if there is another player on turn update the onturn
            self.parent_game=  data['onturn']
        if 'restart' in data:
            self.parent_game.start(on_turn = data['restart']['onturn'])
        

    def send(self, data):
        data = bytes(json.dumps(data), "utf-8")
        self.c.send(data)

class Game(Tk):
    def __init__(self):
        super().__init__(screenName="Tic tac toe")
        self.client = None
        self.start()
        self.show_menu()

    def start(self, on_turn = 1):
        self.board = [[0 for i in range(3)] for i in range(3)]
        self.on_turn = on_turn

    def draw_board(self):
        pass

    def update_board(self):
        pass

    def show_menu(self):
        self.top_frame = Frame()
        self.top_frame.grid()

        self.options_frame = Frame()
        self.options_frame.grid()

        self.title_lbl = Label(
            master=self.top_frame,
            text="Tic tac toe",
            font="arial 20"
        )
        self.title_lbl.grid()

        self.join_button = Button(
            master=self.options_frame,
            text="Join",
            font='arial 15',
            width=10,
            command= lambda : self.join_screen()
        )
        self.join_button.grid(row=0, column=0)

        self.host_button = Button(
            master=self.options_frame,
            text="Host",
            font='arial 15',
            width=10,
            command= lambda : self.host()
        )
        self.host_button.grid(row=0, column=1)

    def join_screen(self):
        self.options_frame.destroy()
        self.title_lbl.config(text="Join")

        self.entries_frame = Frame()
        self.entries_frame.grid()

        self.entry_lbl = Label(
            master=self.entries_frame,
            text="IP adress:"
        )
        self.entry_lbl.grid()

        self.ip_entry = Entry(
            master=self.entries_frame,
            font='arial 15',
            width=20
        )
        self.ip_entry.grid()

        self.join_button = Button(
            text="join",
            font='arial 15',
            width=20,
            command= lambda : self.join()
        )
        self.join_button.grid()

    def host(self):
        pass

    def join(self):
        global IP 
        
        try:
            IP = int(self.ip_entry.get())
        except ValueError:
            messagebox.showerror("ERROR", "Invalid IP")
            self.join_screen()

if __name__ == "__main__":
    global game
    game = Game()
    game.mainloop()