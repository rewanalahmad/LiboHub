from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse

def ordermethod(request):
    return HttpResponse('order')

def orderitemmethod(request):
    return HttpResponse("orderitem")