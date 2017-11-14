import random
import platform
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    if not session.get('gold'):
        # session['gold'] = int((random.random() * (100 - 0 + 1)))
        session['gold'] = 0
        session['activity'] = ""

    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/process_money', methods=['post'])
def process_money():
    # get the source
    source = request.form['location']

    if source == 'farm':
        foundGold = int((random.random() * 10) + 10)
        session['gold'] += foundGold
        session['activity'] += "Earned " + str(foundGold) + " golds from the farm!\n"
    elif source == 'cave':
        foundGold = int((random.random() * 5) + 5)
        session['gold'] += foundGold
        session['activity'] += "Earned " + str(foundGold) + " golds from the cave!\n"
    elif source == 'house':
        foundGold = int((random.random() * 2) + 2)
        session['gold'] += foundGold
        session['activity'] += "Earned " + str(foundGold) + " golds from the house!\n "
    elif source == 'casino':
        toss = random.random()
        if toss >= 0.5:
            winner = True
        else:
            winner = False

        amountWon = int((random.random() * 50))
        if winner:
            session['gold'] += amountWon
            session['activity'] += "Won " + str(amountWon) + " golds at the casino!\n"
        else:
            session['gold'] -= amountWon
            session['activity'] += "Lost " + str(amountWon) + " golds at the casino! Ouch!\n"

    return redirect("/")

if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
