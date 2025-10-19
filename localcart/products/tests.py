from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category
from django.db.models import Avg,Count,Sum,Q
from django.template import loader

#go to Queryset API for more featuers

def categoray_view(request):
    c=Category.objects.filter(name='soul')
    print(c)
    return HttpResponse('CATEGORAY')

def products_view(request):
    c=Product.objects.filter(name='it ends with us').exclude(name__contains='soul').order_by("-created_at")
    agg=Category.objects.aggregate(Count('id'))
    three_items=Category.objects.all()[:3] #it will print only first 3 items
    a=Category.objects.filter(Q(name__startswith='R')|Q(name__startswith='F')) #Q is for complex operations 
    values=Category.objects.filter(name='Romanc').values() #vlaues() it shows all informations

    print(values)
    return HttpResponse("products")



def categoray(requeast):
    """
    this method represent all categoray u have in your Database.
    """
    template=loader.get_template("categoray.html")
    categoray=Category.objects.all().values()
    context={

        'categoray':categoray
    }
    return HttpResponse(template.render(context,requeast))

def order(request,id):
    template=loader.get_template("orders.html")
    order=Order.objects.filter(id=id)
    product=Product.objects.get(pk=id)
    context={
        "order":order,
        "product":product
    }
    return HttpResponse(template.render(context,request))


def product(requast):
    template=loader.get_template('index.html')
    product=Product.objects.all()
    context={
        "product":product
    }
    return HttpResponse(template.render(context,requast))


class Productlistview(ListView):
    '''
    this class will show the product model as list.
    '''
    model=Product
    template_name='index.html'
    context_object_name='pro'
    def get_queryset(self):
        """
        this method make sure the deta we reciving is filtterd.
        the point here it's overrirden this class.
        """
        filtter_product=Product.objects.filter(name='it ends with us')
        return filtter_product
    


class productdetails(DetailView):
    """
    this class will show the product list as link u can clicked and get the details.
    it dosn't work without id
    """
    model=Product
    template_name='product_details.html'
    context_object_name='product'

class Spicificproductview(View):
    def get(self,request,*args,**kwargs):
        #fetch producta with love in description.
        love_products=Product.objects.filter(description__contains='love')
        context={
            "love":love_products
        }
        return render(request,'refreshing_prod.html',context)

