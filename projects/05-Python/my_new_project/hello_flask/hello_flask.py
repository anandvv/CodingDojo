import platform
from flask import Flask, render_template

# create an "app" variable which represents our web application.
app = Flask(__name__)


# we are attaching the hello_world function to the '/' route
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
