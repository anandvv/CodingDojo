import re

from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector


app = Flask(__name__)
app.secret_key = "GottaHaveASecret"

mysql = MySQLConnector(app, 'mydb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    # get all the emails and pass it to the index page
    getEmails = "SELECT email FROM emails"
    emails = mysql.query_db(getEmails)

    return render_template('index.html', emails=emails)


@app.route('/addemail', methods=["POST"])
def addemail():
    email = request.form['email']
    if len(email) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):  # do some regex and check if email is valid
        flash("Invalid Email Address!")
    else:
        # check to see if the email already exists in the database
        query = "SELECT * FROM emails WHERE email = :specificEmail"
        data = {'specificEmail': email}
        users = mysql.query_db(query, data)
        if users:
            flash("Email already exists!")
        else:
            # insert the email into the database
            insert_query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:specificEmail, now(), now())"
            insert_data = {'specificEmail': email}
            mysql.query_db(insert_query, insert_data)
            flash("Success!")

    return redirect("/")


@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')


app.run(debug=True)