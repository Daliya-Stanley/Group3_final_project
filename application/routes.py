from flask import render_template, url_for, request, redirect,jsonify, flash, session
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
    user_email = session.get('user_email')
    first_name = get_first_name_by_email(user_email) if user_email else "Traveller"
    return render_template('wheel_of_fortune.html', first_name=first_name)

@app.route('/wheel')
def wheel():
    user_id = session.get('user_id')
    first_name = get_first_name_by_id(user_id) if user_id else "Traveller"
    return render_template('wheel.html', first_name=first_name)

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
    user_email = session.get('user_email')
    first_name = get_first_name_by_email(user_email) if user_email else "Adventurer"
    return render_template('rock_paper_scissors.html', first_name=first_name)


@app.route('/rock_paper_scissors', methods=['POST'])
def play():
    player_choice = request.form['user_choice']
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return jsonify({'computer_choice': computer_choice, 'result': result})

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

            return redirect(url_for('rock_paper_scissors'))
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

            flash("Login successful! Welcome back 🎉", "success")
            return redirect(url_for('rock_paper_scissors'))
        else:
            # Login failed: show error message
            error = result["message"]

    return render_template('login.html',
                           form=login_form,
                           message=error,
                           title_head='Login',
                           next=next_page)

@app.route('/logout')
def logout():
    session.pop('user_email', None)  # remove the user from the session
    flash("You've been logged out 👋", "info")
    return redirect(url_for('login'))


@app.route('/mulan')
def mulan_page():
      return render_template('mulan.html')


















@app.route('/Arendelle')
def frozen_page():
    return render_template('frozen_fantasia.html', title_head='Arandelle holidays', title_body='The Frozen Magical Land of Arandelle!!', subtitle='★ Come and explore the known and unknown magical powers of Arandelle★', img="static/images/frozen_main.jpeg")

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
        cursor.execute("""SELECT
            e.ExperienceName,
            e.ExperiencePrice,
            e.ExperienceImage,
            b.BookingDate
        FROM BookingExperience as b
        INNER JOIN Experiences e ON b.ExperienceID = e.ExperienceID
        WHERE b.ExperienceID = %s""", (experience_id,))
        experience =cursor.fetchone()
        if experience:
            name, price, image, date = experience
            total = quantity * price
            total_price += total

            experiences_in_cart.append(
                {'experienceid': experience_id, 'experiencename': name, 'experienceprice': price, 'experienceimage': image, 'datereserved':date,
                'quantity': quantity, 'total': total})
    conn.close()
    return render_template ('cart.html', products=products_in_cart, experiences= experiences_in_cart, total= total_price)

@app.route('/add_to_cart_experience/<int:experience_id>', methods=['POST'])
def add_to_cart_experience(experience_id):
    if 'cart' not in session:
        session['cart'] = {'products': {}, 'experiences': {}}
    cart = session['cart']
    exp_cart = cart['experiences']

    if str(experience_id) in exp_cart:
        exp_cart[str(experience_id)] += 1
    else:
        exp_cart[str(experience_id)] = 1

    session['cart']['experiences'] = exp_cart

    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    insert_experience_booking(experience_id, booking_date, booking_time)

    flash("Booking successful! Magical Experience added to cart! Continue shopping or go to view your cart!", "success")
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

        if item_type == 'experiences':
            try:
                delete_latest_booking(item_id)
            except Exception as e:
                flash(f'Error deleting booking: {e}', 'danger')
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


#context processor is used to inject the cart_count variable into the context of every template rendered by the application
@app.context_processor
def cart_item_count():
    cart = session.get('cart', {'products': {}, 'experiences': {}})
    count = sum(cart['products'].values()) + sum(cart['experiences'].values())
    return dict(cart_count=count)



@app.route('/wonderland')
def wonderland():
    return render_template('wonderland.html', title_head='Wonderland', title_body='Wonderland', subtitle='Want to wander in Wonderland?', img='static/images/WT.jpg')


@app.route('/aquariel')
def aquariel():
    cards = [
  {
    "title": "Dive into Ariel’s World",
    "short_text": "Swirl through a glowing whirlpool and glide past singing seahorses.",
    "text": "Begin your adventure by swirling through a glowing whirlpool and arriving in Aquariel. Glide past colorful reefs and singing seahorses as you discover the ocean’s most magical secrets.",
    "img": "whirlpool_dive.jpg",
    "alt": "Whirlpool Dive"
  },
  {
    "title": "Rest like royalty in the Pearl Palace",
    "short_text": "Sleep beneath pearlescent domes and wake to coral melodies.",
    "text": "Sleep beneath pearlescent domes, lulled by the lullabies of the sea. The Pearl Palace in Aquariel offers serene beauty, with soft coral beds and gentle currents outside your window.",
    "img": "coral_room.jpg",
    "alt": "Undersea Room"
  },
  {
    "title": "Dine under the sea with magical flavors",
    "short_text": "Taste sea blossom soufflés and starfruit sushi beneath the waves.",
    "text": "Taste the wonders of Aquariel—sea blossom soufflés, starfruit sushi, and mermaid-made desserts. Every bite is a spell, every dish a dream.",
    "img": "undersea_feast.jpg",
    "alt": "Underwater Feast"
  },
  {
    "title": "Explore the glittering Aquariel Bazaar",
    "short_text": "Find charms, sea stones, and sunken wonders from the deep.",
    "text": "Discover treasures from sunken ships, enchanted sea stones, and hand-crafted mermaid charms. The Aquariel Bazaar is where magic meets memory.",
    "img": "undersea_market.jpg",
    "alt": "Undersea Market"
  },
  {
    "title": "Celebrate Aquariel's oceanic wonders",
    "short_text": "Join jellyfish lantern parades and the Shell Symphony.",
    "text": "Join the Festival of Tides, the Shell Symphony, and glowing jellyfish lantern parades. Aquariel's culture is a dance of joy, melody, and color beneath the waves.",
    "img": "festival_of_tides.jpg",
    "alt": "Undersea Festival"
  },
  {
    "title": "Embrace enchantment in every bubble",
    "short_text": "Follow ancient sea runes and befriend dolphins of legend.",
    "text": "Follow shimmering currents, discover ancient sea runes, and chat with dolphins who know the secrets of the deep. Aquariel is where imagination breathes through every ripple.",
    "img": "undersea_exploration.jpg",
    "alt": "Mystical Exploration"
  }]
    return render_template(
        'aquariel.html',
        cards=cards,
        hero_title="Welcome to Aquariel",
        hero_subtitle="Dive into a world where wonder glows beneath the waves",
        intro_title="Follow Ariel into a realm where curiosity reigns and sea stars guide your way!",
        css_file="aquariel.css"
    )


@app.route('/book_destination')
def book_destination():
    return render_template('book_magical_destination.html', title_head='Book Your Holiday', title_body='Ready to Book you Magical Adventure!', subtitle='This is where your dreams come true!')


