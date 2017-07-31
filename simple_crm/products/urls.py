from django.conf.urls import url
from products.views import ProductsCreateView, create

urlpatterns = [
    url(r'^create/$', create, name='product_create'),
]