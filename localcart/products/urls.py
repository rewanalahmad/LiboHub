from django.urls import path
from products import views

app_name='Products'
urlpatterns=[
    path('',views.index,name='index'),
    path('test/',views.test,name='test'),
    #categoray related
    path('add_categoray/',views.add_category_forms,name="add_category"),
    path('add_categoray/<int:categoray_id>/',views.add_product,name='add_product_with_genre'),
    #product related
    path('add_product/',views.add_product_forms,name="add_product"),
    path('feedback/',views.feedbackFrom,name='add_feedback'),
    path('<int:id>',views.product_name_by_id,name='product'),
    path("thank-you/",views.thank_you,name="thank_you"),

]