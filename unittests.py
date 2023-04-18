import unittest
from tic_tac_toe import *

class TestTicTacToe(unittest.TestCase):
    def test_display_board(self):
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        expected_output = "X|O|X\nO|X|O\nX|O|X\n"
        self.assertEqual(display_board(board), expected_output)
        

