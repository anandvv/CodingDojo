import platform

from flask import Flask, render_template, redirect, request, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "GottaHaveASecret"

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'twitter')
# an example of running a query
print mysql.query_db("SELECT * FROM users")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
