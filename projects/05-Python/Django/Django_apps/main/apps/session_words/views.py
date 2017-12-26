from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
    return render(request, 'session_words/index.html')


def process(request):

    if request.method == "POST":
        word = request.POST['word']
        color = request.POST['color']
        isBig = request.POST.get('isBig', "unchecked")
        if isBig == "checked":
            bigFont = True
        else:
            bigFont = False

    lineItem = {
        "word": word,
        "color": color,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "isBig": bigFont
    }

    if not 'words' in request.session or not request.session['words']:
        request.session['words'] = [lineItem]
        # print "Session: ", request.session['words']
    else:
        saved_words = request.session['words']
        # print "Before Append: ", saved_words
        saved_words.append(lineItem)
        # print "After Append: ", saved_words
        request.session['words'] = saved_words

    return render(request, 'session_words/index.html')


def clear(request):
    request.session['words'] = []
    return render(request, 'session_words/index.html')

