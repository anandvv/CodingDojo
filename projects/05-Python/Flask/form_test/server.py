import platform
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # redirects back to the '/' route
    return redirect('/show')


@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
