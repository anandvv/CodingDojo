import re

from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "GottaHaveASecret"

mysql = MySQLConnector(app, 'mydb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    if not session.get('userid'):
        session['userid'] = -1

    data = {'id': session['userid']}

    select_query = "SELECT * FROM users WHERE id = :id"
    user = mysql.query_db(select_query, data)

    if user:
        session['username'] = user[0]['username']

    return render_template('index.html')


@app.route('/logout', methods=['GET'])
def logout():
    session['userid'] = -1
    return redirect("/")


@app.route('/login', methods=['POST'])
def create():
    # add a friend to the database!
    username = request.form['username']
    password = request.form['password']

    if username == "":
        flash("Username cannot be empty!")
        return redirect("/")

    if password == "":
        flash("Password cannot be empty!")
        return redirect("/")

    data = {'login': username}

    select_query = "SELECT * FROM users WHERE username = :login"
    user = mysql.query_db(select_query, data)

    if user:
        if bcrypt.check_password_hash(user[0]['password'], password):
            # login user
            session['userid'] = user[0]['id']
            session['username'] = user[0]['username']
            flash("Successful login!")
            # get all posts
            query = "SELECT * FROM posts p " \
                    "JOIN users u " \
                    "ON p.user_id = u.id " \
                    "ORDER BY p.created_at DESC"
            posts = mysql.query_db(query)
            return render_template('index.html', posts=posts)
        else:
            # set flash error message and redirect to login page
            flash("Incorrect password")
            return redirect('/')
    else:
        flash("User not found, please register!")
        return redirect('/register')


@app.route('/register', methods=['GET'])
def register():
    if session['userid'] > 0:
        flash('User logged in!')
        return redirect('/')

    return render_template('/register.html')


@app.route('/registrations', methods=['POST'])
def registerNewUser():
    username = request.form['username']
    password = request.form['password']
    passwordConfirmation = request.form['passwordConfirmation']
    email = request.form['email']

    if len(username) < 2:
        flash('username cannot be less than 2 characters')

    # TODO add a regex to check for alphabets only for username

    # TODO add a regex to check for alphanumeric only for password

    if password != passwordConfirmation:
        flash("passwords don't match")
        return redirect('/register')

    if len(email) < 1:
        flash("Email cannot be blank!")
        return redirect('/register')
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        return redirect('/register')

    pw_hash = bcrypt.generate_password_hash(password)

    insert_query = "INSERT INTO users (username, password, email, created_at, updated_at) " \
                   "VALUES (:username, :pw_hash, :email, NOW(), NOW())"
    query_data = {'username': username, 'pw_hash': pw_hash, 'email': email}
    session['userid'] = mysql.query_db(insert_query, query_data)
    print session['userid']
    # redirect to success page
    return redirect('/')


app.run(debug=True)
