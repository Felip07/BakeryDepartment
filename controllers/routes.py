from flask import render_template, url_for, redirect, request
import urllib

def init_app(app):
    
    @app.route("/")
    def home():
        return render_template('index.html')