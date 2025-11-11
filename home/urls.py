from django.urls import path
from home import views

app_name='home'
urlpatterns=[
    path('',views.index,name='homepage'),
    path('about/',views.about_us,name='about_us'),
    path('contactus/',views.contactus,name="contactus")
]