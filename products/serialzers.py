from rest_framework import serializers
from .models import Product,Category
from django.contrib.auth.models import User

class UserSerialzers(serializers.HyperlinkedModelSerializer):
    #product=serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    product = serializers.HyperlinkedRelatedField(
        many=True, read_only=True,view_name="product"
    )
    class Meta:
        model=User
        fields=['id','username','product']

class CategoraySerialzers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ProductSerialzers(serializers.HyperlinkedModelSerializer):
    user=UserSerialzers(read_only='True')
    categoray= CategoraySerialzers(read_only='True')
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="productVit", format="html"
    )
    #favorited_by=UserSerialzers(read_only='True',many='True')
    class Meta:
        model=Product
        fields=['id','name','description','categoray','price','stock','imag', 'user',
                'style','owner','highlight']
        read_only_fields=['imag']