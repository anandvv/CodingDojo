import platform

from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "GottaHaveASecret"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users/<username>')
def show_user_profile(username):
    return render_template("user.html", username=username)


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)