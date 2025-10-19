from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Order,OrderItem

def ordermethod(request):
    #order=Order.objects.filter(Order__name__exact='Romanc')
    #order_ex=Order.objects.exclude(paid=True)
    order_ex=Order.objects.exclude(paid=True)
    return HttpResponse('order')

def orderitemmethod(request):

    return HttpResponse("orderitem")