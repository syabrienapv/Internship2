from unicodedata import name
from main import app
import os
from flask import request, redirect, render_template

@app.route('/')
def index():
    return render_template('index.html')