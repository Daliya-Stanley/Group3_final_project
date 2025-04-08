from flask import render_template, url_for, request, redirect

from application import app


@app.route('/')
def home_page():
    return render_template('home.html', title_head='Enchanted Getaway Travels', title_body='Enchanted Getaway Travels', subtitle='★ Travel the unexplored lands ★', img="static/images/wallpaper_home.jpeg")





























































@app.route("/cinderella_kingdom")
def cinderella_kingdom():
    return render_template(
        "cinderellas_kingdom.html", title_head="Cinderella's Kingdom", title_body='Far Far Away!', subtitle='★ Welcome to the destination where wishes come true ★', img="images/cinderella.jpg"
    )










