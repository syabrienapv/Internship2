from unicodedata import name
from main import app
import os
from flask import Flask, request, redirect, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def test_form():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    return render_template('index.html', teks=processed_text) 