from flask import render_template, url_for, request, redirect,jsonify, flash, session
from application.forms.register_form import RegistrationForm
from application.forms.login_form import LoginForm
from application.data_access import *
from application import app
from datetime import timedelta
import os

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
    promotional_products = get_promotional_products()
    first_name = get_first_name_by_email(user_email) if user_email else "Traveller"
    return render_template('wheel_of_fortune.html', first_name=first_name, promotional_products = promotional_products) #html=python variable


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
            session['user_id'] = result["user_id"]

            if remember:
                session.permanent = True  # Make the session persistent

            flash("Login successful! Welcome back 🎉", "success")
            if not next_page or next_page == 'None':
                next_page = url_for('rock_paper_scissors')
            return redirect(next_page)
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
    session.clear()
    session.pop('user_email', None)  # remove the user from the session
    flash("You've been logged out 👋", "info")
    return redirect(url_for('login'))


@app.route('/mulan')
def mulan_page():
      return render_template('mulan.html')



@app.route('/Product')
def product_page():
    product_list = get_products()
    purchased = get_total_purchased_by_product()

    for product in product_list:
        pid = str(product['productid'])
        product['stock_remaining'] = max(0, 5 - purchased.get(pid, 0))

    return render_template(
        'product.html',
        title_head='Magical Products',
        title_body='Our Splendid Magical Products',
        subtitle='★ The Magical Things Which You Always Wished For!★',
        img="static/images/product_background.jpeg",
        products=product_list
    )

@app.route('/Experience')
def experience_page():
    experience_list = get_experience()
    image_dir = os.path.join(app.static_folder, "images")
    gallery_images = sorted([
        filename for filename in os.listdir(image_dir)
        if filename.startswith("gallery") and filename.lower().endswith((".jpg", ".png", ".jpeg", ".webp"))
    ])
    return render_template('experience2.html', title_head='Magical Experience', experiences = experience_list,gallery_images=gallery_images)


@app.route('/add_product_to_cart/<int:product_id>', methods=['GET', 'POST'])
def add_product_to_cart(product_id):
    session.setdefault('cart', {'products': {}, 'experiences': {}, 'destinations': {}})
    session.setdefault('product_cart', [])

    product_cart_dict = session['cart']['products']
    current_qty = product_cart_dict.get(str(product_id), 0)
    quantity_to_add = int(request.form.get('quantity', 1))

    # Calculate remaining stock
    total_purchased = get_total_purchased_by_product()
    purchased_qty = total_purchased.get(str(product_id), 0)
    stock_remaining = max(0, 5 - purchased_qty)

    # Enforce stock cap
    if current_qty + quantity_to_add > stock_remaining:
        flash(f"Only {stock_remaining - current_qty} items left in stock!", "warning")
        return redirect(url_for('product_page'))

    product_cart_dict[str(product_id)] = current_qty + quantity_to_add
    session['cart']['products'] = product_cart_dict

    # Product details
    product = get_product_details(product_id)
    user_id = session.get('user_id')

    # Update product_cart or append
    for item in session['product_cart']:
        if item['productid'] == product_id:
            item['quantity'] += quantity_to_add
            break
    else:
        session['product_cart'].append({
            'productid': int(product_id),
            'quantity': quantity_to_add,
            'user_id': user_id,
            'productname': product[0],
            'productprice': product[1],
            'productimage': product[2],
            'stockremaining': int(stock_remaining)
        })

    session.modified = True
    flash(f"{quantity_to_add} item(s) added to cart! 🎁", "success")
    return redirect(url_for('product_page') + "#product-cards")


@app.route('/update_quantity/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    new_quantity = int(request.form.get('quantity'))
    product_id_str = str(product_id)
    purchased = get_total_purchased_by_product()
    stock_remaining = max(0, 5 - purchased.get(product_id_str, 0))

    if not (1 <= new_quantity <= stock_remaining):
        flash(f"Quantity must be between 1 and {stock_remaining}.", "warning")
        return redirect(url_for('view_cart'))

    # Update quantity in session cart
    session.setdefault('cart', {'products': {}, 'experiences': {}, 'destinations': {}})
    session['cart']['products'][product_id_str] = new_quantity

    # Update quantity in detailed product_cart
    for item in session.get('product_cart', []):
        if item['productid'] == product_id:
            item['quantity'] = new_quantity
            break

    session.modified = True
    flash("Quantity updated!", "success")
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    experience_cart = session.get("experience_cart", [])
    product_cart = session.get("product_cart", [])


    products_in_cart = []
    experiences_in_cart = []
    total_price = 0

    conn = get_db_connection()
    cursor = conn.cursor()

    for item in product_cart:
        total = item['quantity'] * item['productprice']
        item['total'] = total
        products_in_cart.append(item)
        total_price += total

    for item in experience_cart:
        total = item['guests'] * item['experienceprice']
        item['total'] = total
        item['quantity'] = item['guests']
        item['datereserved'] = item['booking_date']
        experiences_in_cart.append(item)
        total_price += total

    cursor.close()
    conn.close()

    return render_template(
        'cart.html',
        products=products_in_cart,
        experiences=experiences_in_cart,
        total=total_price
    )


@app.route('/add_to_cart_experience/<int:experience_id>', methods=['POST'])
def add_to_cart_experience(experience_id):
    guests = int(request.form['guests'])
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    user_id = request.form['user_id']

    # Fetch max group size
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ExperienceGroupSize FROM Experiences WHERE ExperienceID = %s", (experience_id,))
    max_guests = cursor.fetchone()[0]

    if guests > max_guests:
        flash(f"Max group size for this experience is {max_guests}. You tried to book {guests}.", "warning")
        return redirect(url_for('experience_page'))

    # Initialize carts
    session.setdefault('cart', {'products': {}, 'experiences': {}, 'destinations': {}})
    session.setdefault('experience_cart', [])

    # Check if this experience is already booked by user
    for item in session['experience_cart']:
        if item['experience_id'] == experience_id and str(item['user_id']) == str(user_id):
            flash("⚠️ You’ve already booked this magical experience!", "warning")
            return redirect(url_for('experience_page'))

    # Add to simple cart
    session['cart']['experiences'][str(experience_id)] = 1

    # Get experience info
    cursor.execute("SELECT ExperienceName, ExperiencePrice, ExperienceImage FROM Experiences WHERE ExperienceID = %s", (experience_id,))
    experience = cursor.fetchone()
    name, price, image = experience

    # Add to detailed cart
    session['experience_cart'].append({
        'experience_id': experience_id,
        'user_id': user_id,
        'booking_date': booking_date,
        'booking_time': booking_time,
        'guests': guests,
        'experiencename': name,
        'experienceprice': price,
        'experienceimage': image
    })

    session.modified = True
    flash("Magical Experience added to cart!", "success")
    return redirect(url_for('experience_page'))

@app.route('/checkout', methods=['POST'])
def checkout():
    experience_cart = session.get('experience_cart', [])
    product_cart = session.get('product_cart', [])

    if not experience_cart and not product_cart:
        flash("Cart is empty!", "warning")
        return redirect(url_for('view_cart'))

    user_id = session.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Orders (UserID) VALUES (%s)", (user_id,))
        order_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()

        process_order_items(order_id, product_cart, experience_cart, user_id)

        # Clear the cart
        session['product_cart'] = []
        session['experience_cart'] = []
        session['cart'] = {'products': {}, 'experiences': {}, 'destinations': {}}

        flash("Your magical order has been placed! 🎉", "success")
        return redirect(url_for('order_receipt', order_id=order_id))

    except Exception as e:
        flash(f"Checkout failed: {str(e)}", "danger")
        return redirect(url_for('view_cart'))

@app.route('/order_receipt/<int:order_id>')
def order_receipt(order_id):
    order_info = get_order_info(order_id)
    products = get_ordered_products(order_id)
    experiences = get_ordered_experiences(order_id)

    return render_template('order_receipt.html',
                           order=order_info,
                           products=products,
                           experiences=experiences,
                           order_id=order_id)



@app.route('/availability', methods=['POST'])
def check_availability():
    data = request.get_json()
    experience_id = data['experience_id']
    booking_date = data['booking_date']
    booking_time = data['booking_time']
    remaining = get_remaining_spots(experience_id, booking_date, booking_time)
    return jsonify({"remaining_spots": remaining})


@app.route('/remove_from_cart/<item_type>/<int:item_id>')
def remove_from_cart(item_type, item_id):
    cart = session.get('cart', {'products': {}, 'experiences': {}, 'destinations': {}})
    item_id_str = str(item_id)

    # Remove from main cart dictionary
    if item_type in cart and item_id_str in cart[item_type]:
        del cart[item_type][item_id_str]
        session['cart'] = cart

    # Remove from detailed session cart
    if item_type == 'products':
        session['product_cart'] = [item for item in session.get('product_cart', []) if item.get('productid') != item_id]
    elif item_type == 'experiences':
        session['experience_cart'] = [item for item in session.get('experience_cart', []) if item.get('experience_id') != item_id]

    session.modified = True
    flash(f'{item_type.capitalize()} removed from cart!', 'info')
    return redirect(url_for('view_cart'))

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
    cards = [
        {
            "title": "Embark on a journey where curiosity is your guide",
            "short_text": "Take your first steps towards Wonderland and tumble down the rabbit hole into the unexpected...",
            "text": "Begin your journey to Wonderland by tumbling down the rabbit hole, where the elusive 'Drink Me' potion awaits, ready to shrink you through a tiny door. What lies on the other side? A world of secrets, magic, and endless wonder — waiting to be discovered",
            "img": "W-rabbithole.jpg",
            "alt": "Rabbit Hole"
        },
        {
            "title": "Sleep like a dormouse in whimsical luxury",
            "short_text": "This enchanting hotel room immerses you in the magic of Alice’s adventures, with every corner brimming with playful charm. ",
            'text':'Soft, glowing lanterns cast a warm, purple-hued light across the room, creating a cozy atmosphere that feels both fantastical and serene. The Queen of Hearts might rule the garden, but in here, you’ll rest easy—far from her watchful eye. Whether you’re seeking adventure or simply a whimsical retreat, this room offers a perfect blend of luxury and playful wonder.',
            "img": "W-bedroom.jpg",
            "alt": "Wonderland Room"
        },
        {
            "title": "Dining in Wonderland is anything but ordinary",
            "short_text": "Step into a surreal setting where teacups float mid-air, cakes are stacked impossibly high, and menus come with riddles instead of descriptions.",
            "text": "Every meal is a mad celebration of flavor, fantasy, and fun. From enchanted garden picnics to candlelit feasts beneath glowing toadstools, each dining space is a feast for the senses. Expect playful presentations, surprise bites, and flavors that spark your curiosity. One thing’s for sure, in Wonderland, dining is a delicious kind of madness.",
            "img": "W-food2.jpg",
            "alt": "Wonderland Feast"
        },
        {
            "title": "Step into the curiously charming shopping quarter of Wonderland",
            "short_text": "Meander through cobbled paths lined with crooked chimneys and signs that change when you're not looking.",
            "text": "Peek into the Mad Hatter’s Hat Emporium for eccentric headwear, or pick up enchanted trinkets and 'Drink Me' bottles that glow softly on the shelves. At the Queen of Hearts’ Boutique, find heart-shaped accessories and red velvet treasures fit for a royal tantrum, while the White Rabbit’s Clock Stop offers curious timepieces that run forward, backward, and sometimes sideways. Potion shops bubble with mysterious concoctions, and whimsical bakeries serve edible souvenirs too pretty to eat (but too tempting not to)",
            "img": "W-shop2.jpg",
            "alt": "Wonderland Shops"
        },
        {
            "title": "Witness the Spring Bloom Parade and dance at The Twilight Toadstool Ball",
            "short_text": "Wonderland’s celebrations invite you to step out of the ordinary and into the extraordinary — where laughter is loud and the party never ends. Curiosity required. Sense of time? Optional.",
            "text": "Join the Spring Bloom Parade and watch flowers march with confetti falling from the sky, or indulge in the whimsical chaos of the Mad Hatter’s Unbirthday Bash, complete with endless tea and cake. Experience royal elegance at the Queen’s Royal Jubilee, where flamingo croquet and red roses abound, or dance the night away at the Twilight Toadstool Ball, surrounded by glowing mushrooms and starlit desserts. Finally, embrace the playful mystery of the Midnight Mischief Festival, following the Cheshire Cat through a maze of glowing riddles and trickster performances. ",
            "img": "W-twilight.jpg",
            "alt": "Twilight Toadstool Ball"
        },
        {
            "title": "Play the day away in Wonderland",
            "short_text": "Lose your logic and find your fun in a delightfully upside down world",
            "text": "From the moment you arrive, reality takes a backseat and imagination takes the wheel. The air hums with mischief and marvel. Teacups spin midair, flowers whisper secrets, and music seems to come from the trees themselves. Whether you're exploring glowing mushroom forests or solving riddles to unlock hidden doors, every moment is interactive and immersive. Time doesn’t matter here; tea is served all day, it’s always someone’s unbirthday, and spontaneity reigns.",
            "img": "W-vibe.jpg",
            "alt": "Wonderland Vibes"
        }]
    return render_template(
        'wonderland2.html',
        cards=cards,
        hero_title="Welcome to Wonderland",
        hero_subtitle="Down the rabbit hole you go, into a world where magic and curiosity collide!",
        intro_title="Ready to tumble into tea parties, talking cats, and total nonsense?",
        css_file="wonderland2.css"
    )


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
        css_file="aquariel.css",
    )


@app.route('/book_destination')
def book_destination():
    return render_template('book_magical_destination.html', title_head='Book Your Holiday', title_body='Ready to Book you Magical Adventure!', subtitle='This is where your dreams come true!')

# @app.route('/Arendelle')
# def frozen_page():
#     return render_template('frozen_fantasia.html', title_head='Arandelle holidays', title_body='The Frozen Magical Land of Arandelle!!', subtitle='★ Come and explore the known and unknown magical powers of Arandelle★', img="static/images/frozen_main.jpeg")



@app.route('/Arendelle')
def frozen_page():
    cards = [
  {
    "title": "Our Luxurious Rooms",
    "short_text": "",
    "text": "A lavish, Frozen-themed castle chamber adorned with icy elegance and a crackling fireplace, blending royal comfort with enchanting beauty.",
    "img": "frozen_luxury.jpeg",
    "alt": "Frozen room"
  },
  {
    "title": "Our Magnificent Views",
    "short_text": "",
    "text": "The palace offers a breathtaking view of the shimmering sea and a glistening ice ring, sparkling under the sky like a scene from a winter fairytale.",
    "img": "frozen_skating.jpeg",
    "alt": "Castle View"
  },
  {
    "title": "Our Succulent and Luscious Spread",
    "short_text": "",
    "text": "The castle delights guests with exquisite cuisine, enchanting desserts, magical drinks, and impeccable royal service fit for a fairytale.",
    "img": "frozen_food.jpeg",
    "alt": "Arendalle Feast"
  },
  {
    "title": "Our beautiful Markets",
    "short_text": "",
    "text": "Discover the enchanting Winter Market, a beautiful and amazing wonderland filled with twinkling lights, festive stalls, seasonal treats, and heartwarming holiday charm.",
    "img": "frozen_market.jpeg",
    "alt": "Winter Market"
  },
  {
    "title": "Our World Class Entertainment",
    "short_text": "",
    "text": "Step into the Frozen Theme Castle where fun, dance, culture, and dazzling entertainment come to life in a magical celebration!",
    "img": "frozen_entertainment.jpeg",
    "alt": "Undersea Festival"
  },
  {
    "title": "Magical Experience",
    "short_text": "",
    "text": " Experience winter magic at the Frozen Theme Resort with snowman building and thrilling sledging adventures for all ages!",
    "img": "frozen_experience.jpeg",
    "alt": "Mystical Exploration"
  }]
    return render_template(
        'frozen_fantasia.html',
        cards=cards,
        video="/video/frozen_main.mp4",
        hero_title="Arandelle holidays",
        hero_subtitle="The Frozen Magical Land of Arandelle!!",
        intro_title="★ Come and explore the known and unknown magical powers of Arandelle★",
        css_file="frozen_styles.css"
    )


































































@app.route('/about_us')
def about_us():
    return render_template('about_us_page.html', title_head='EGT Magical Team',
                           title_body='Magical Team of Enchanted Getaways! ',
                           subtitle='★ We make your dreams come true★',
                           img="static/images/wallpaper_home.jpeg")
