import platform
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "ItsGotToBeASecret"

@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    propertyBag = {}
    propertyBag['name'] = request.form['name']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect("/")

    propertyBag['dojoLocation'] = request.form['dojoLocation']
    propertyBag['favoriteLanguage'] = request.form['favoriteLanguage']
    propertyBag['comment'] = request.form['comment']
    print "Comment Length: ", len(request.form['comment'])
    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        return redirect("/")

    if len(request.form['comment']) > 120:
        flash("Comments too long. Keep it under 120 characters!")
        return redirect("/")
    # print name, dojoLocation, favoriteLanguage, comment

    return render_template("result.html", propertyBag=propertyBag)


if __name__ == '__main__':
    # Check the System Type before to decide to bind
    # If the system is a Linux machine -:)
    if platform.system() == "Linux":
        app.run(host='127.0.0.1', port=5000, debug=True)
    # If the system is a windows /!\ Change  /!\ the   /!\ Port
    elif platform.system() == "Windows":
        app.run(host='127.0.0.1', port=50000, debug=True)
