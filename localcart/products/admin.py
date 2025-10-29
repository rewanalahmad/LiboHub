from django.contrib import admin
from .models import Product,Category,FeedBack

class categoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    search_fields=['name']

class productadmin(admin.ModelAdmin):
    list_display=['categoray','name','slug','description','price','stock',
                  'imag','created_at']
class feednackadmin(admin.ModelAdmin):
    list_display=['name','email','feedback','satisfaction']


admin.site.register(Category,categoryadmin)
admin.site.register(Product,productadmin)
admin.site.register(FeedBack,feednackadmin)