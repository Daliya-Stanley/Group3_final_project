from flask import render_template, url_for, request, redirect,jsonify, Blueprint
from mysql.connector import cursor

from application import app

import random

from application.data_access import mydb


@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")

# @app.route('/')
# def home():
#     return render_template()

@app.route('/wheel_of_fortune')
def wheel_of_fortune_game():
    return render_template('wheel_of_fortune.html')



def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/rock_paper_scissors')
def rps_game():
    history = mydb.get_game_history()
    return render_template('rps.html', history=history)

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    mydb.save_game(player_choice, computer_choice, result)
    history = mydb.get_game_history()
    return jsonify({'computer_choice': computer_choice, 'result': result, 'history': [{'player': h[0], 'computer': h[1], 'outcome': h[2], 'time': str(h[3])} for h in history]})