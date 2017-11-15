import platform
import re

from flask import Flask, render_template, redirect, request, session, flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "GottaHaveASecret"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['post'])
def process():
    if len(request.form['email']) < 1:
        flash("Email is a required field!")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not in the appropriate format!")
    if len(request.form['firstName']) < 1:
        flash("First Name is required!")
        if len(request.form['lastName']) < 1:
            flash("Last Name is required!")
    if not request.form['firstName'].isalpha() or not request.form['lastName'].isalpha():
        flash("First and Last Names cannot contain non-alphabetic characters!")
    if len(request.form['password']) < 1:
        flash("Password is required!")
    if len(request.form['password']) > 8:
        flash("Password cannot be more than 8 characters!")
    if len(request.form['passwordConfirmation']) < 1:
        flash("Password Confirmation is required!")
    if  request.form['password'] != request.form['passwordConfirmation']:
        flash("Passwords don't match!")

    return redirect("/")


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)