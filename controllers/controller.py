from app import app
from flask import render_template, request, redirect
from models.game import Game
from models.player import Player

@app.route('/rps')
def index():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def game_played():
    player_1 = Player('Player 1', request.form['player1choice'])
    player_2 = Player('Player 2', request.form['player2choice'])
    live_game = Game(player_1, player_2)
    return render_template('result.html', game=live_game, winner=live_game.play_game())

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play', methods=['POST'])
def play_game():
    player_1 = Player(request.form['name'], request.form['choice'])
    player_2 = None
    comp_game = Game(player_1, player_2)
    player_2 = comp_game.generate_computer_player()
    comp_game = Game(player_1, player_2)
    return render_template('result.html', game=comp_game, winner=comp_game.play_game())