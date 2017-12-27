from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'items': [{ 'id': 1234,
                    'name': 'Dojo Tshirt',
                   'price': 19.99,
                   'qty': [1, 2, 3]},
                  {'id': 1239,
                   'name': 'Dojo Sweater',
                   'price': 29.99,
                   'qty': [1, 2, 3, 4, 5]},
                  {'id': 1243,
                   'name': 'Dojo Cup',
                   'price': 4.99,
                   'qty': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
                  {'id': 1252,
                   'name': 'Algorithm Book',
                   'price': 49.99,
                   'qty': [1, 2, 3, 4, 5, 6, 7, 8]}
                  ]
    }
    return render(request, "amadon/index.html", context)

def process(request):
    print request.method
    if request.method == "POST":
        quantity = request.POST['quantity']
        product_id = request.POST['product_id']
        #do some processing
        context = {
            'total': 323.00,
            'message': 'Thanks for your purchase! Your total is: '
        }

        return redirect(request, "/thankyou")

def thankyou(request):
    return render(request, "amadon/thankyou.html")