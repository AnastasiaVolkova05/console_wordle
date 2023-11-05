import unittest
from program import Game_menu, This_game

class TestThisGame(unittest.TestCase):
    def setUp(self):
        self.some_game = This_game('score')
        self.some_game.attempt += 4
        self.answer = ['something']
    def test_reboot(self):
        self.some_game.reboot('score')
        self.assertEqual(self.some_game.attempt, 0)
        self.assertEqual(self.some_game.answer, [])

if __name__ == "__main__":
    unittest.main()
