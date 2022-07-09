class Game:
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2

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
        
        return f"{winning_player.name} wins by playing {winning_player.choice}"
