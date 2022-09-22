from  django.urls import path

from . import views

app_name='cart'

urlpatterns=[
    path('',views.card_detail,name='cartdetail'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('remove/<int:product_id>/',views.cart_remove,name='removecart'),
    path('delete/<int:product_id>/',views.full_delete,name='fulldelete')
]