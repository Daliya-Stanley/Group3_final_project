from flask import render_template, url_for, request, redirect,jsonify, Blueprint
from mysql.connector import cursor
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application import app

import random



@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels',
                           title_body='Enchanted Getaway Travels',
                           subtitle='★ Travel the unexplored lands ★',
                           img="static/images/wallpaper_home.jpeg")


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

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    error = ""

    if request.method == 'POST':
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        # Here you would call a function to add the user, e.g.:
        # add_person(username, email, password)

        return redirect(url_for('welcome'))

    return render_template('register.html',
                           form=register_form,
                           message=error,
                           title_head='Register',
                           title_body='Register',
                           img="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = ""

    if request.method == 'POST':
        username = login_form.username.data
        password = login_form.password.data
        # Logic to verify the user would go here
        # If successful, redirect to a welcome page or dashboard

    return render_template('login.html',
                           form=login_form,
                           message=error,
                           title_head='Login')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')




































@app.route('/Arendelle')
def frozen_page():
    return render_template('frozen_fantasia.html', title_head='Arandelle holidays', title_body='The Frozen Magical Land of Arandelle!!', subtitle='★ Come and explore the known and unknown magical powers of Arandelle★', img="static/images/frozen_main.jpeg")

@app.route('/Experience')
def experience_page():
    return render_template('experience.html', title_head='Magical Experience', title_body='Do what you always wished for!', subtitle='★ What once was in your dreams in now coming true★', img="static/images/Experience_background.jpeg")

@app.route('/Product')
def product_page():
    return render_template('product.html', title_head='Magical Products', title_body='Our Splendid Magical Products', subtitle='★ The Magical Things Which You Always Wished For!★', img="static/images/product_background.jpeg")




















@app.route('/wonderland')
def wonderland():
    return render_template('destination1.html', title_head='Wonderland', title_body='Wonderland', subtitle='Want to wander in Wonderland?', img='static/images/WT.jpg')






































































































































































































































































































































































































































































































































































































































































































































































































@app.route("/cinderella_kingdom")
def cinderella_kingdom():
    destination = get_destination_by_name("Cinderella’s_Kingdom")
    cards = [
  {
    "title": "Attend the Grand Ball",
    "short_text": "",
    "text": "Dress in your finest attire and dance the night away. Join fellow guests for a night of enchanting music, delightful dances and a chance to meet magical characters!",
    "img": "grand_ball.jpg",
    "alt": "Guests dancing at the Grand Ball"
  },
  {
    "title": "Explore the Enchanted Gardens",
    "short_text": "",
    "text": "Wander through the beautiful Enchanted Gardens, where every flower tells a tale. Enjoy magical picnics or simply relax admist the fragrant blooms filled with butterflies.",
    "img": "enchanted_gardens.jpg",
    "alt": "Beautiful flowers"
  },
{
    "title": "Meet the Fairy godmother",
    "short_text": "",
    "text": "Get a chance to meet your very own Fairy godmother. She’s ready to sprinkle a little magic into your life! Share your dreams and see them come to pass with her help.",
    "img": "fairy_godmother.jpg",
    "alt": "Fairy godmother assisting guests"
  },

  {
    "title": "The Mystical Cinderella Carriage",
    "short_text": "",
    "text": "Shimmering chariot woven from moonlight and magic, where dreams take flight. Take a ride on the carriage Cinderella rode to meet her Prince Charming.",
    "img": "carriage3.jpg",
    "alt": "Beautiful carriage"
  },
    {
    "title": "Vanishing Glass Slippers",
    "short_text": "",
    "text": "Race against time in this exquisite Glass Slippers, for in them lie a fairy tale waiting to be awakened!",
    "img": "glass_slippers.jpg",
    "alt": "Beautiful Glass Slippers"
  },
  {
    "title": "Magical Mystery Dress",
    "short_text": "",
    "text": " Adorned with sparkling gems and twinkling fairy dust, this magical dress transforms a person into royalty!",
    "img": "magic_dress.jpg",
    "alt": "Cinderella’s Dress"
  }]
    return render_template(
        "cinderellas_kingdom.html",
        cards=cards,
        hero_title="Cinderella's Kingdom",
        hero_subtitle="The Mystical Cinderella’s Kingdom",
        intro_title="★ The Destination where wishes come true★",
        css_file="cinderella.css",
        destination=destination
)


