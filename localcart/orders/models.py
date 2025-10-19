from django.db import models
from products.models import Product
from django.conf import settings

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,
                           null=True,blank=True,default=0)
    created=models.DateTimeField(auto_created=True,blank=True,null=True)
    paid=models.BooleanField(default=False)
    total=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,
                              default=0.00)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE,
                            null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,default=None)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,
                              default=0.00)
    quantity= models.PositiveIntegerField(default=1)