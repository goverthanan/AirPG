from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# @ signifies its a decorator
# Using decorator we can wrap a python function and modify its behaviour
@app.route('/')
@app.route('/index')
def index():
    return "Goverthanan Flask Web app"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form[username] != "admin":
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route('/submit')
def submit():
    return render_template("submit.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
