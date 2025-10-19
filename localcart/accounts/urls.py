from django.urls import path,include
from .views import register
from accounts import views
app_name='accounts'
urlpatterns=[
    path('register/',views.register ,name='register'),
    path('', include('django.contrib.auth.urls'))
]