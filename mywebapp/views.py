from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def services(request):
    our_services = ['bush camps','balloon tours', 'village visits','yoga']
    price = 10000
    date = '15-12-2024'
    return render( request,'services.html', context={'our_services':our_services, 'price':price, 'date':date})


def about(request):

    return render( request,'about.html')


