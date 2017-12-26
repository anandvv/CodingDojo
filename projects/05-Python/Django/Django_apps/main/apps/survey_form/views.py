from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'survey_form/index.html')


def create(request):
    if request.method == "POST":
        if 'attempt' in request.session:
            print "using the existing session object", request.session['attempt']
            request.session['attempt'] += 1

        else:
            print "creating attempt session object"
            request.session['attempt'] = 1

        context = {
            "name": request.POST['name'],
            "favorite_language": request.POST['language'],
            "location": request.POST['location'],
            "comment": request.POST['comment'],
            "attempt": request.session['attempt']
        }

        return render(request, 'survey_form/result.html', context)




