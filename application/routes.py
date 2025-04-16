from flask import render_template, url_for, request, redirect,jsonify, flash, session
from mysql.connector import cursor
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application.data_access import *
from application import app
from datetime import timedelta

app.permanent_session_lifetime = timedelta(days=30)

import random
if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="login"
    )
    return mydb

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels',
                           title_body='Enchanted Getaway Travels',
                           subtitle='★ Travel the unexplored lands ★',
                           img="static/images/wallpaper_home.jpeg")


@app.route('/wheel_of_fortune')
def wheel_of_fortune_game():
    user_email= session.get('user_email')
    first_name = "Traveller"
    if user_email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT FirstName FROM User WHERE Email = %s", (user_email,))
        result = cursor.fetchone()
        if result:
            first_name = result[0].capitalize()

        cursor.close()
        conn.close()

    return render_template('wheel_of_fortune.html', first_name=first_name)




def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
@app.route('/rock_paper_scissors')
def rock_paper_scissors():
    user_email = session.get('user_email')
    first_name = "Adventurer"
    if user_email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT FirstName FROM User WHERE Email = %s", (user_email,))
        result = cursor.fetchone()
        if result:
            first_name = result[0].capitalize()

        cursor.close()
        conn.close()

    return render_template('rock_paper_scissors.html', first_name=first_name)



@app.route('/rock_paper_scissors', methods=['POST'])
def play():
    player_choice = request.form['user_choice']
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return render_template('rock_paper_scissors.html', title_head='Rock Paper Scissors',
                           title_body='Rock Paper Scissors!!',
                           subtitle='★ Rock Paper Scissors ★',
                           computer_choice=computer_choice,
                           user_choice=player_choice,
                           result=result)



@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    error = ""

    if request.method == 'POST':
        firstname = register_form.firstname.data
        lastname = register_form.lastname.data
        email = register_form.email.data
        password = register_form.password.data

        result = register_person(firstname, lastname, email, password)

        if result["success"]:
            flash(result["message"], "success")

            session['user_email'] = result["email"]

            session.permanent = True  # Make the session persistent
            app.permanent_session_lifetime = timedelta(days=30)

            return redirect(url_for('home_page'))
        else:
            error = result["message"]

    return render_template('register.html',
                           form=register_form,
                           message=error,
                           title_head='Register',
                           title_body='Register',
                           img="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    #the request.args.get('next') gets the value of the parameter next during a GET request
    #when we submit a POST request via the form the request.args.get('next') no longer contains 'next'
    #so because of the <input type="hidden" name="next" value="{{ next }}"> that exists in the login form the value of the variable 'next' is stored
    #and we get its value through the request.form.get('next')
    next_page = request.args.get('next') or request.form.get('next')
    error = ""

    if request.method == 'POST':
        email = login_form.email.data
        password = login_form.password.data
        remember = login_form.remember_me.data

        result = authenticate_user(email, password)

        if result["success"]:
            # Login success: store session info and redirect
            session['user_email'] = result["email"]

            if remember:
                session.permanent = True  # Make the session persistent
                app.permanent_session_lifetime = timedelta(days=30)

            flash("Login successful! Welcome back 🎉", "success")
            return redirect(url_for('home_page'))
        else:
            # Login failed: show error message
            error = result["message"]

    return render_template('login.html',
                           form=login_form,
                           message=error,
                           title_head='Login')

@app.route('/logout')
def logout():
    session.pop('user_email', None)  # remove the user from the session
    flash("You've been logged out 👋", "info")
    return redirect(url_for('login'))


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')

@app.route('/wheel')
def wheel():
    user_id = session.get('user_id')
    first_name = "Traveller"

    if user_id:
        conn = mysql.connector.connect(
            host='localhost',
            user='your_user',
            password='your_pass',
            database='your_db'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT first_name FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            first_name = result[0]
        cursor.close()
        conn.close()

    return render_template('wheel.html', first_name=first_name)
















@app.route('/mulan')
def mulan_page():
      return render_template('mulan.html', title_head="mulan's World", title_body="Whispers of Mulan's World.", subtitle='★ Enjoy a mystical retreat where destiny, beauty, and bravery meet ★')


















@app.route('/Arendelle')
def frozen_page():
    return render_template('frozen_fantasia.html', title_head='Arandelle holidays', title_body='The Frozen Magical Land of Arandelle!!', subtitle='★ Come and explore the known and unknown magical powers of Arandelle★', img="static/images/frozen_main.jpeg")

# @app.route('/Experience')
# def experience_page():
#     return render_template('experience.html', title_head='Magical Experience', title_body='Do what you always wished for!', subtitle='★ What once was in your dreams in now coming true★', img="static/images/Experience_background.jpeg")

@app.route('/Product')
def product_page():
    product_list = get_products()
    return render_template('product.html', title_head='Magical Products', title_body='Our Splendid Magical Products', subtitle='★ The Magical Things Which You Always Wished For!★', img="static/images/product_background.jpeg", products = product_list)

@app.route('/Experience')
def experience_page():
    experience_list = get_experience()
    return render_template('experience.html', title_head='Magical Experience', title_body='Our Splendid Magical Experience', subtitle='★ What once was in your dreams in now coming true★', img="static/images/Experience_background.jpeg", experiences = experience_list)


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {'products': {}, 'experiences': {}}
    cart = session['cart']
    product_cart = cart['products']

    if str(product_id) in product_cart:
        product_cart[str(product_id)] += 1
    else:
        product_cart[str(product_id)] = 1

    session['cart']['products']= product_cart
    print("Cart after adding", session['cart'])
    flash("🪄 Product added to cart! Continue shopping or go to view your cart! ", "success")
    return redirect(url_for('product_page'))


# @app.route('/remove_from_cart/<int:product_id>')
# def remove_from_cart(product_id):
#     product_cart = session.get('cart', {})
#
#     if str(product_id) in product_cart:
#         del product_cart[str(product_id)]
#         session['cart']['products'] = product_cart
#         flash('Product removed from cart!', 'info')
#
#     return redirect(url_for('view_cart'))


@app.route('/cart')
def view_cart():
    cart = session.get("cart", {})
    products_in_cart = []
    experiences_in_cart = []
    total_price = 0

    if not cart or (not cart.get('products') and not cart.get('experiences')):
        return render_template('cart.html', products=[], experiences=[], total=0)

    conn = get_db_connection()
    cursor = conn.cursor()

    total_price = 0

    for product_id, quantity in cart['products'].items():
        cursor.execute("Select ProductName, ProductPrice, ProductImage from Product Where ProductID =  %s",(product_id,))
        product=cursor.fetchone()
        if product:
            name, price,image = product
            total = quantity * price
            total_price += total

            products_in_cart.append({'productid': product_id, 'productname': name, 'productprice': price,'productimage': image, 'quantity': quantity, 'total': total})


    for experience_id,quantity in cart ['experiences'].items():
        cursor.execute("Select ExperienceName, ExperiencePrice, ExperienceImage, DateReserved from Experiences where ExperienceID = %s", (experience_id,))
        experience =cursor.fetchone()
        if experience:
            name, price, image, date = experience
            total = quantity * price
            total_price += total

            experiences_in_cart.append(
                {'experienceid': experience_id, 'experiencename': name, 'experienceprice': price, 'experienceimage': image, 'date':date,
                'quantity': quantity, 'total': total})
    conn.close()
    return render_template ('cart.html', products=products_in_cart, experiences= experiences_in_cart, total= total_price)

@app.route('/add_to_cart_experience/<int:experience_id>')
def add_to_cart_experience(experience_id):
    if 'cart' not in session:
        session['cart'] = {'products': {}, 'experiences': {}}
    cart = session['cart']
    exp_cart = cart['experiences']

    if str(experience_id) in exp_cart:
        exp_cart[str(experience_id)] += 1
    else:
        exp_cart[str(experience_id)] = 1

    session['cart']['experiences']= exp_cart
    print("Cart after adding", session['cart'])
    flash("🪄 Magical Experience added to cart! Continue shopping or go to view your cart! ", "success")
    return redirect(url_for('experience_page'))

@app.route('/remove_from_cart_experience/<int:experience_id>')
# def remove_from_cart_experience(experience_id):
#     exp_cart = session.get('cart', {})
#
#     if str(experience_id) in exp_cart:
#         del exp_cart[str(experience_id)]
#         session['cart']['experiences'] = exp_cart
#         flash('Magical Experience removed from cart!', 'info')
#
#     return redirect(url_for('view_cart'))

@app.route('/remove_from_cart/<item_type>/<int:item_id>')
def remove_from_cart(item_type, item_id):
    cart = session.get('cart', {'products': {}, 'experiences': {}})

    # Convert item_id to string to match the cart key format
    item_id_str = str(item_id)

    if item_type not in cart:
        flash('Invalid item type', 'danger')
        return redirect(url_for('view_cart'))

    if item_id_str in cart[item_type]:
        del cart[item_type][item_id_str]
        session['cart'] = cart
        flash(f'{item_type.capitalize()} removed from cart!', 'info')
    else:
        flash(f'{item_type.capitalize()} not found in the cart.', 'warning')

    return redirect(url_for('view_cart'))

# @app.route('/cart')
# def view_cart_experience():
#     cart = session.get("cart", {})
#     experience_in_cart = []
#
#     if not cart:
#         return render_template('cart.html',experiences= [], total=0)
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     total_price = 0
#     for experience_id, quantity in cart.items():
#         cursor.execute("Select ExperienceName, ExperiencePrice, ExperienceImage, DateReserved from Experiences Where ExperienceID =  %s",(experience_id,))
#         experience=cursor.fetchone()
#         if experience:
#             name, price,image, date = experience
#             total = quantity * price
#             total_price += total
#
#             experience_in_cart.append({'experienceid': experience_id, 'experiencename': name, 'experienceprice': price,'experienceimage': image, 'datereserved' : date, 'quantity': quantity, 'total': total})
#     return render_template ('cart.html', experiences=experience_in_cart, total= total_price)

# @app.route('/remove_from_cart/<item_type>/<int:item_id>')
# def remove_from_cart(item_type, item_id):
#     cart = session.get('cart', {})
#     item_key = str(item_id)
#     if item_key in cart:
#         del cart[item_key]
#         session['cart'] = cart
#         flash(f"{item_type.title()} removed from cart.", "info")
#     return redirect(url_for('view_cart_experience'))

@app.route('/product_sale')
def product_sale():
    if 'user_email' in session:
        user_email= session['user_email']
        return render_template('product.html', user_email=user_email, title='Logged In Adventurer')
    return render_template('product_sale.html', user_email=False, title='Login Area')











@app.route("/cinderella_kingdom")
def cinderella_kingdom():
    return render_template(
        "cinderellas_kingdom.html",
        title_head="Cinderella's Kingdom",
        title_body='Far Far Away!',
        subtitle='★ Welcome to the destination where wishes come true ★',
        img="static/images/cinderella.jpg"
    )







@app.route('/wonderland')
def wonderland():
    return render_template('destination1.html', title_head='Wonderland', title_body='Wonderland', subtitle='Want to wander in Wonderland?', img='static/images/WT.jpg')

@app.route('/aquariel')
def aquariel():
    return render_template('aquariel.html', title_head='Aquariel', title_body='Aquariel', subtitle='Where tides whisper secrets beneath the sea foam')

