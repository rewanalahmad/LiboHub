from django.contrib import admin
from .models import Order,OrderItem


class orderadmin(admin.ModelAdmin):
    list_display=('id','user','created','paid','total')
    search_fields=['user']

class itemorder(admin.ModelAdmin):
    list_display=('order','product','price','quantity')

admin.site.register(Order,orderadmin)
admin.site.register(OrderItem,itemorder)