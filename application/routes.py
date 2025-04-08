from flask import render_template, url_for, request, redirect

from application import app

@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaways', title_body='Enchanted Getaways', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")




















































@app.route('/wonderland')
def wonderland():
    return render_template('destination1.html', title_head='Wonderland', title_body='Wonderland', subtitle='Want to wander in Wonderland?', img='static/images/WT.jpg')


