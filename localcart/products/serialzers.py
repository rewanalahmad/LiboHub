from rest_framework import serializers
from .models import Product,Category
from django.contrib.auth.models import User

class UserSerialzers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class CategoraySerialzers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ProductSerialzers(serializers.ModelSerializer):
    user=UserSerialzers(read_only='True')
    categoray= CategoraySerialzers(read_only='True')
    #favorited_by=UserSerialzers(read_only='True',many='True')
    class Meta:
        model=Product
        fields=['id','name','description','categoray','price','stock','imag', 'user']
        read_only_fields=['imag']

