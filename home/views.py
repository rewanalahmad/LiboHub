from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from products.models import Product,Category
from django.views.generic import ListView,DetailView,View

# Create your views here.
class productdetails(DetailView):
    """
    this class will show the product list as link u can clicked and get the details.
    it dosn't work without id
    """
    model=Product
    template_name='homepage.html'
    context_object_name='product'

def index(request):
    template=loader.get_template('homepage.html')
    product=Product.objects.all()
    categoray=Category.objects.all()
    context={
        'product':product,"categoray":categoray
    }
    return render(request,'homepage.html',context)

def about_us(request):
    return render(request,'about.html',{})

def contactus(request):
    return render(request,'contactus.html',{})