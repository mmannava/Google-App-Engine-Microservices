from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/split-traffic')
def split_traffic():
    return render_template('split-traffic.html')