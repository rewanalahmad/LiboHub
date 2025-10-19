from django.http import HttpResponse
from .models import Product,Category,FeedBack
from django.db.models import Avg,Count,Sum,Q
from django.template import loader
from orders.models import Order
from django.views.generic import ListView,DetailView,View
from .forms import ProductForm,FeedbackForm,CategoryForm
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required


def add_product(request,categoray_id=None):
    categoray=None
    if categoray_id:
        #categoray=Category.objects.get(id=categoray_id)
        categoray=get_object_or_404(Category,id=categoray_id)
        form=ProductForm(request.POST or None,initial= {'categoray':categoray}) 
    else:
        form=ProductForm(request.POST or None)
    if  request.method=='POST' and form.is_valid():
        new_product=form.save()
        return redirect("Products:product",categoray_id=new_product.categoray.id)
    context={
        'form':form, "categoray":categoray
    }
    return render(request,'add_new_product.html',context)


def add_category_forms(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Products:index')  # or 'Products:home' if you want to show products
    else:
        form = CategoryForm()
    
    context = {'form': form}
    return render(request, "add_categoray.html", context)

def add_product_forms(request):
    if request.method =="POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Products:index")
        
    else:
        form=ProductForm()
    product=Product.objects.all().values()
    context={'form':form, "product":product}
    return render(request,"add_product.html",context)

def index(request):
    template=loader.get_template('index.html')
    product=Product.objects.all()
    categoray=Category.objects.all()
    context={
        'product':product,"categoray":categoray
    }
    return HttpResponse(template.render(context,request))

def test(request):
    return render(request,'test.html')


def product_name_by_id(request,id):
    '''
    this method represent when u call the spicific name of product ,
    by calling his id in url in your broswer.
    it's not user frendly
    '''
    template=loader.get_template('product.html')
    product=Product.objects.get(id=id) #u can't put it in for i html it's not iteratabil.
    context={
        'product':product
    }
    return HttpResponse(template.render(context,request))



def feedbackFrom(request):
    '''
    this method it's spose save it in admin but it didn't work, and the thank page too.
    '''
    if request.method=='POST':
        print(request.POST)
        form = FeedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #process the form
            print(form.cleaned_data)
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            feedback=form.cleaned_data['feedback']
            satisfaction=form.cleaned_data['satisfaction']
            FeedBack.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                satisfaction=satisfaction
            )
            return redirect('Products:thank_you')
    else:
        form=FeedbackForm()
    context={'form':form}
    return render(request,'feedback.html',context)

def thank_you(requast):
    return HttpResponse('thank you for your feedback')


