#Notes:
#It contains the url patters which are used to match with the incoming url requests.

from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('hello/',views.index),   
    path('products/',views.products,name="products"),
    path('products/<int:id>',views.product_details,name="product_details"),
    path('products/add/',views.add_product,name="add_product"),
    path('products/update/<int:id>',views.update_product,name="update_product"),
    path('products/delete/<int:id>',views.delete_product,name="delete_product"),
    path('products/mylistings',views.my_listings,name="mylistings"),

]
