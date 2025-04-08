from flask import render_template, url_for, request, redirect
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application import app


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")

<<<<<<< HEAD
@app.route('/register', methods=['GET', 'POST'])
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
=======




























































@app.route("/cinderella_kingdom")
def cinderella_kingdom():
    return render_template(
        "cinderellas_kingdom.html", title_head="Cinderella's Kingdom", title_body='Far Far Away!', subtitle='★ Welcome to the destination where wishes come true ★', img="images/cinderella.jpg"
    )










>>>>>>> Daphne
