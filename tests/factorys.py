import factory
from django.contrib.auth.models import User
from products.models import Product,Category
from faker import Faker

faker= Faker()

class UserFactoray(factory.django.DjangoModelFactory):
    class Meta:
        model=User
    
    username=faker.name()
    is_staff ='True'

class CategorayFactoray(factory.django.DjangoModelFactory):
    class Meta:
        model=Category

class ProductFactoray(factory.django.DjangoModelFactory):
    class Meta:
        model=Product

    name="it ends with us"
    categoray=factory.SubFactory(CategorayFactoray)
    description=faker.text()
    slug='product_slug'
    price=0.00
    stock=0.00
