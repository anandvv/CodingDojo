import platform
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html", phrase="Hello", times=5)


@app.route('/ninjas')
def ninjas():
  return render_template("ninjas.html")


@app.route('/dojos/new')
def newdojo():
  return render_template("dojos.html")


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
