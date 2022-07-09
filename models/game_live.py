from player import Player
from game import Game

player_1 = Player('Player 1', 'paper')
player_2 = Player('Player 2', 'paper')

live_game = Game(player_1, player_2)

print(live_game.play_game())