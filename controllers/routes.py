from flask import render_template, url_for, redirect, request
from models.database import db, Padaria
import urllib

def init_app(app):
    
    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/retaguarda")
    def retaguarda():
        padariaestoque = Padaria.query.all()
        return render_template('retaguarda.html', padariaestoque = padariaestoque)
    
    @app.route("/add", methods=["GET", "POST"])
    def add():
        if request.method == "POST":
            return redirect(url_for('index'))
    return render_template("add.html")