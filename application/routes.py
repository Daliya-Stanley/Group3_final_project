from flask import render_template, url_for, request, redirect

from application import app


@app.route('/')
def home_page():
    return render_template('home.html', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")


@app.route('/destination2')
def destination2():
    return render_template('destination2.html', title_head='Kingdom Cinderella', title_body='Welcome to Kingdom Cinderella, where your dreams come true', subtitle="Your dream is one wish away", img="static/images/magicwish.jpg")
