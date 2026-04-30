from django.http import HttpResponse,HttpResponseForbidden
from .models import Product,Category,FeedBack
from django.db.models import Avg,Count,Sum,Q
from django.template import loader
from .forms import ProductForm,FeedBackForm,CategoryForm
from comment.models import Comment
from comment.forms import CommentsForms
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages,sessions
from rest_framework import viewsets
from .serialzers import ProductSerialzers,UserSerialzers
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadonly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import generics


@login_required()
def add_product(request,categoray_id=None):
    inital_data={}
    categoray=None
    if categoray_id:
        #categoray=Category.objects.get(id=categoray_id)
        categoray=get_object_or_404(Category,id=categoray_id)
        inital_data={"categoray":categoray}
        #form=ProductForm(request.POST or None,initial= {'categoray':categoray}) 
    if  request.method=='POST' :
        form=ProductForm(request.POST,request.FILES, initial=inital_data)
        if form.is_valid(): 
            new_product=form.save()
            return redirect("home:homepage",categoray_id=new_product.categoray.id)
    else:
        form=ProductForm(initial=inital_data) 
    product=Product.objects.all()
    context={
        'form':form, "categoray":categoray,"product":product
    }
    return render(request,'add_product.html',context)

@login_required()
def add_category_forms(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Products:add_category')  # or 'Products:home' if you want to show products
    else:
        form = CategoryForm()
    
    context = {'form': form}
    return render(request, "add_categoray.html", context)

@login_required()
def add_product_forms(request):
    if request.method =="POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Products:add_product")
        
    else:
        form=ProductForm()
    product=Product.objects.all().values()
    context={'form':form, "product":product}
    return render(request,"add_product.html",context)



def product(request,id):
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


@login_required()
def feedbackForm(request):
    request.session['feedback_visit']=request.session.get('feedback_visit',0)+1
    '''
    this is for deleting a session:

    if "feedback_visit" in request.session:
        del request.session['feedback_visit']
    this is for clear:
        request.session.clear()
    when u use this it will like reset the sesseion to 0
        request.session.flush()
    '''

    if request.method == 'POST':
        form = FeedBackForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            satisfaction = form.cleaned_data['satisfaction']

            FeedBack.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                satisfaction=satisfaction
            )
            #messages.add_message(request,messages.SUCCESS,"Feedback sent successfully")
            messages.success(request,'Feedback sent successfully')#another way "faster"
            return redirect('home:homepage')
    else:
        form =FeedBackForm()
        context={'form':form,
                 'visits':request.session['feedback_visit'] }
    return render(request, 'feedback.html',context)


def comment_on_product(request,id):
    '''
    this method for comment on the spicific book(product)
    '''
    template=loader.get_template('comment.html')
    product=get_object_or_404(Product,id=id)
    comment=product.comments.all()
    new_comment=None

    if request.method =='POST':
        comment_form=CommentsForms(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product= product #we relate to product bec we have forgien key relate
            new_comment.user=request.user
            new_comment.save()
            return redirect(product.get_absolute_url())#it will refresh the page itself
    else:
        comment_form=CommentsForms()
    context={'product':product,
              'comment':comment,
              "comment_form":comment_form}
    return HttpResponse(template.render(context,request))

def search_results(request):
    query=request.GET.get('query','')
    results=[]
    if query:
        #results=Product.objects.filter(name__icontains=query) if query else []
        results=Product.objects.filter(
        Q(name__icontains=query)|
        Q(description__icontains=query)|
        Q(categoray__name__icontains=query))
        seen_id=()
        uniq_results=[]
        for result in results:
            if result.id not in seen_id:
                uniq_results.append(result)

    else:
        uniq_results=[]
    context={'query':query, "results":results}
    return render(request,'search_result.html',context)


def feedbackForm_v2(request):
    request.session['feedback_visit']=request.session.get('feedback_visit',0)+1

    if request.method == 'POST':
        form = FeedBackForm(request.POST, request.FILES)
        if form.is_valid():
            #save form data to session
            request.session['feedback_data']=form.cleaned_data
            return redirect('Products:feedback_review')
    else:
        form =FeedBackForm()
        context={'form':form,
                 'visits':request.session['feedback_visit'] }
    return render(request, 'feedback.html',context)

def feedback_review(request):
    #create feedback data
    feedback_data= request.session.get('feedback_data',{})
    if request.method=="POST":
        FeedBack.objects.create(**feedback_data)
        del request.session['feedback_data']
        return redirect("home:homepage")

    form=FeedBackForm(initial=feedback_data)
    return render(request,'feedback_review.html',{'form':form})

@login_required()
def toggle_favorite(request,id):
    product=get_object_or_404(Product,id=id)
    if request.user in product.favorited_by.all():
        product.favorited_by.remove(request.user)
    else:
        product.favorited_by.add(request.user)

    return redirect("Products:product",id=id)

@login_required()
def favorite_products(request):
    user=request.user
    favorite=user.favorit_book.all()
    return render(request,'favorite.html',{'products':favorite})

def categoray_view(request,categoray_name):
    products = Product.objects.filter(categoray__name__icontains=categoray_name)
    return render(request,"categoray_name.html",{'products':products})
    
@login_required()
def delete_product(request,id):
    product= get_object_or_404(Product,id=id)
    #checkif the cuurent user is the owner of the cretaing this product(the superuser)
    if not request.user == product.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method=='POST':
        product.delete()
        return redirect('home:homepage')
    
    context={'product':product}
    return render(request,'delete.html',context)

def edit_product(request, id):
    product=get_object_or_404(Product,id=id)
    if not request.user == product.user and not request.user.is_superuser:
        return HttpResponse("not allowed")
    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("Products:product",  id=id)
    else:
        form=ProductForm(instance=product)
    context={"form":form, 'product':product}
    return render(request,"edit_form.html",context)


class productViewSet(viewsets.ModelViewSet):

    queryset=Product.objects.all() # wich object should be manage.
    serializer_class=ProductSerialzers # wich serialzer should convert to json.
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadonly]
'''
    def perform_create(self, serializer):
        """ this is part form ModelViewSet"""
        serializer.save(user=self.request.user)        
        serializer.save(owner=self.request.user) #now will be passed an additional 'owner' field
'''



