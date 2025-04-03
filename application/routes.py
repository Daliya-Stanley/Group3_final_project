from flask import render_template, url_for, request, redirect

from application import app


@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaways', title_body='Enchanted Getaways', subtitle='★ travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")
