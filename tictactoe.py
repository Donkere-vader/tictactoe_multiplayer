from tkinter import Label, Tk, Button, Entry, Frame
import socket
import threading
import json


IP = "0.0.0.0"
PORT = 69420


class Client:
    def __init__(self, host: bool):
        self.host = host

    def start(self):
        pass

    def send(self, data):
        data = bytes(json.dumps(data), "utf-8")
        self.c.send()

class Game(Tk):
    def __init__(self):
        super().__init__(screenName="Tic tac toe")
        self.board = [[0 for i in range(3)] for i in range(3)]
        self.on_turn = 1
        self.show_menu()

    def draw_board(self):
        pass

    def update_board(self):
        pass

    def show_menu(self):
        top_frame = Frame()
        top_frame.grid()

        options_frame = Frame()
        options_frame.grid()

        Label(
            master=top_frame,
            "test"
        ).grid()

    def join_screen(self):
        pass

    def host(self):
        pass

if __name__ == "__main__":
    global game
    game = Game()
    game.mainloop()