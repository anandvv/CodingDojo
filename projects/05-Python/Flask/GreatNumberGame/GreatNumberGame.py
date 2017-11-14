import random
import platform
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    if not session.get('someKey'):
        session['someKey'] = int((random.random() * (100 - 0 + 1)))

    if not session.get('firstVisit'):
        session['message'] = ''
        session['firstVisit'] = True

    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/', methods=['POST'])
def index_post():

    userGuess = int(request.form['userGuess'])
    print "User Guess: ", userGuess

    if userGuess < int(session['someKey']):
        # print userGuess
        # print "Too low"
        # session.pop('message')
        session['message'] = "Too low"
    elif userGuess > int(session['someKey']):
        # print userGuess
        # print "Too high"
        # session.pop('message')
        session['message'] = "Too high"
    else:
        session['message'] = "Yay! You guessed it."

    return render_template("index.html")


@app.route('/addtwo')
def addtwo():
    session['counter'] += 1

    return redirect("/")


@app.route('/reset')
def reset():
    session['counter'] = 0

    return redirect("/")

if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
