from django.urls import path,include
from products import views
from rest_framework.routers import DefaultRouter
app_name='Products'
router=DefaultRouter() # automatically generates URL patterns
router.register(r'product',views.productViewSet,basename='product')
urlpatterns=[
    #categoray related
    path('add_categoray/',views.add_category_forms,name="add_category"),
    path('add_categoray/<int:categoray_id>/',views.add_product,name='add_product_with_genre'),
    #product related
    path('add_product/',views.add_product_forms,name="add_product"),
    path('feedback/',views.feedbackForm,name='add_feedback'),
    path("review",views.feedback_review,name='feedback_review'),
    path('<int:id>/',views.product,name='product'),
    path("<int:id>/favorit/",views.toggle_favorite,name='toggle_favorite'),
    path("myfavorit/",views.favorite_products,name='favorite_book'),
    path('product_comment/<int:id>',views.comment_on_product,name='comment_on_product'),
    path('search/',views.search_results,name='search'),
    path("romanc_books/<str:categoray_name>",views.categoray_view,name='categoray_name'),
    path("delete/<int:id>",views.delete_product,name='delete'),
    path("edit/<int:id>",views.edit_product,name='edit'),
    #api related
    path('api/',include(router.urls)),

]