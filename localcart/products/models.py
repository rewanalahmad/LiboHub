from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, default="product_name")
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering=['-name']

    def __str__(self):
        return self.name


class Product(models.Model):
    categoray = models.ForeignKey(
        Category,
        related_name='products',   # no spaces in related_name
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150, default="product_name")
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.00   # must be a number, not None
    )
    stock = models.PositiveBigIntegerField(
        default=0  # must be a number, not None
    )
    imag = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    feedbak=models.CharField()
    satisfaction=models.CharField(max_length=50)