from flask import render_template, url_for, request, redirect

from application import app


@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")































@app.route('/frozen_fantasia')
def frozen_page():
    return render_template('frozen_fantasia.html', title_head='Arendelle Enchanted Escape', title_body='Frozen Realms Retreat', subtitle='★ "Join Elsa, Anna, and friends on a frosty journey through a sparkling winter wonderland, where every day is a magical snow day!" ★', img="static/images/frozen_wallpage.jpeg")

# @app.route('/')
# def home():
#     return render_template()