from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def discuss():
    return render_template('discuss.html')