import unittest
from tic_tac_toe import *

class TestTicTacToe(unittest.TestCase):
    def test_next_turn(self):
        global buttons, players, player
        buttons = [[{"text": ""} for j in range(3)] for i in range(3)]
        players = ["X", "O"]
        player = players[0]

        next_turn(0, 0)

        self.assertEqual(buttons[0][0]["text"], players[0])
    
    def test_check_winner(self):
        pass 
    
    def test_check_tie(self):
        pass 
    
    def test_new_game(self):
        pass
    
    def test_ai_play(self):
        pass
    
    def test_make_buttons(self):
        pass




        

