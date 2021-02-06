from django.urls import path
from .views import GetAllProducts

urlpatterns = [
    path('get-products/', GetAllProducts.as_view(), name='get-all-products'),
]
