
from django.urls import path

from ecomapp import views
app_name='ecomapp'

urlpatterns = [

    path('',views.allProducts,name='allproducts'),
    path('<slug:c_slug>/',views.allProducts,name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.proDetail,name='prodetail'),
]
