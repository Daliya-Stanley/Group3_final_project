from flask import render_template, url_for, request, redirect
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application import app


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")

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




































@app.route('/Arendelle')
def frozen_page():
    return render_template('frozen_fantasia.html', title_head='Arandelle holidays', title_body='The Frozen Magical Land of Arandelle!!', subtitle='★ Come and explore the known and unknown magical powers of Arandelle★', img="static/images/frozen_main.jpeg")

@app.route('/Experience')
def experience_page():
    return render_template('experience.html', title_head='Magical Experience', title_body='Do what you always wished for!', subtitle='★ What once was in your dreams in now coming true★', img="static/images/Experience_background.jpeg")

@app.route('/Product')
def product_page():
    return render_template('product.html', title_head='Magical Products', title_body='Our Splendid Magical Products', subtitle='★ The Magical Things Which You Always Wished For!★', img="static/images/product_background.jpeg")
