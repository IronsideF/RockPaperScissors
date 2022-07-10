import random
from models.player import Player

class Game:
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2
        self.choices = ['rock', 'paper', 'scissors']

    def play_game(self):
        game_rules = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        winning_player = None
        if self.player1.choice == game_rules[self.player2.choice]:
            winning_player = self.player2
        elif self.player2.choice == game_rules[self.player1.choice]:
            winning_player = self.player1
        
        if winning_player is not None:
            return f"{winning_player.name} wins by playing {winning_player.choice}"
        else:
            return f"{winning_player} wins, it's a draw!"

    def generate_computer_player(self):
        return Player('Computer', random.choice(self.choices) )
