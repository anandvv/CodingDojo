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
    getfriends_query = "SELECT * FROM fullfriends"
    all_friends = mysql.query_db(getfriends_query)

    return render_template('index.html', friends=all_friends)


@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    data = {'first': first_name,
            'last': last_name,
            'email': email}

    insert_query = "INSERT INTO fullfriends (first_name, last_name, email, created_at, updated_at) " \
                   "VALUES (:first, :last, :email, now(), now())"
    mysql.query_db(insert_query, data)

    return redirect('/')


@app.route('/friends/<friend_id>/edit', methods=['GET'])
def edit(friend_id):
    data = {'friend_id': friend_id}
    select_query = "SELECT * FROM fullfriends WHERE id = :friend_id"
    friend = mysql.query_db(select_query, data)[0]

    return render_template('friend.html', friend=friend)


@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    # update a friend to the database!
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    data = {'id': friend_id,
            'first': first_name,
            'last': last_name,
            'email': email}

    update_query = "UPDATE fullfriends SET first_name = :first, last_name = :last, email = :email WHERE id = :id"
    mysql.query_db(update_query, data)

    return redirect('/')


@app.route('/friends/<friend_id>/delete')
def destroy(friend_id):
    # delete a friend to the database!
    data = {'id': friend_id}

    delete_query = "DELETE FROM fullfriends WHERE id = :id"
    mysql.query_db(delete_query, data)

    return redirect('/')


app.run(debug=True)