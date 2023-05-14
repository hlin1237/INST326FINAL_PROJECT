import unittest
from tkinter import *
from tic_tac_toe import *


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.root = Tk()

    def tearDown(self):
        self.root.destroy()

    def test_new_game(self):
        new_game()
        for row in range(3):
            for col in range(3):
                self.assertEqual(buttons[row][col]["text"], "")
                self.assertEqual(buttons[row][col]["state"], "normal")
                self.assertEqual(buttons[row][col]["bg"], "#F0F0F0")

    def test_check_tie(self):
        for row in range(3):
            for col in range(3):
                if (row, col) not in [(0,0), (1,1), (2,2), (0,2), (2,0)]:
                    buttons[row][col]["text"] = "x"
        self.assertEqual(check_tie(), False)

    def test_check_winner(self):
        buttons[0][0]["text"] = "x"
        buttons[1][0]["text"] = "x"
        buttons[2][0]["text"] = "x"
        self.assertEqual(check_winner(), True)

        buttons[0][1]["text"] = "o"
        buttons[1][1]["text"] = "o"
        buttons[2][2]["text"] = "o"
        self.assertEqual(check_winner(), "o")

    def test_next_turn(self):
        next_turn(0, 0)
        next_turn(1, 0)
        next_turn(0, 1)
        next_turn(1, 1)
        next_turn(0, 2)
        self.assertEqual(label["text"], "x wins")


