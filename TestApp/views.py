from django.shortcuts import render
from django.http import HttpResponse
from TestApp.models import Contact
from TestApp.models import Shop


# Create your views here.
def index(request):
    return render(request,'TestApp/index.html')


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=Contact(name=name,email=email,message=message)
        en.save()
    return render(request,"TestApp/contact.html")

def sale(request):
    return render(request,'TestApp/sale.html')

def blog(request):
    return render(request,'TestApp/blog.html')

def Accesseries(request):
    return render(request,'TestApp/Accesseries.html')

def shop(request):
    shops = Shop.objects.all()
    return render(request,'TestApp/shop.html', {'shops' : shops})

def Login(request):
    return render(request,'TestApp/Login.html')
