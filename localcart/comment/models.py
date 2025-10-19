from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.
class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    text=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"comment by {self.user.username} on {self.product}"