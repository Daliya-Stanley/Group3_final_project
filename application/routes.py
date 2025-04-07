from flask import render_template, url_for, request, redirect,jsonify, Blueprint
from mysql.connector import cursor
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application import app
from mysql.connector import cursor


import random

from application.data_access import mydb


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")


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
def rock_paper_scissors():
      return render_template('rock_paper_scissors.html')


@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return jsonify({'computer_choice': computer_choice, 'result': result})

def register():
    register_form = RegistrationForm()
    error = ""

    if request.method == 'POST':
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        #add_person(first_name, last_name, password)
        return redirect(url_for('welcome'))

    return render_template('register.html',
                           form=register_form,
                           message=error,
                           title_head='register',
                           title_body='register',
                           img="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = ""

    if request.method == 'POST':
        username = login_form.username.data
        password = login_form.password.data


    return render_template('login.html',
                           form=login_form,
                           message=error,
                           title_head='login',
                           )

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')