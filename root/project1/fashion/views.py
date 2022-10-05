from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def index(request):



    prod=Product.objects.all()



    

    return render(request,'index.html',{'prod':prod});

