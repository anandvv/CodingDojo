from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    unique_id = get_random_string(length=14)
    print unique_id
    if 'attempt' in request.session:
        print "using the existing session object", request.session['attempt']
        request.session['attempt'] += 1   
        context = {
        "attempt" : request.session['attempt'],
        "random_word" : unique_id
        }
    else:
        print "creating attempt session object"
        request.session['attempt'] = 1
        context = {
            "attempt" : 1,
            "random_word" : unique_id
        }
    return render(request,'random_word/index.html', context)


