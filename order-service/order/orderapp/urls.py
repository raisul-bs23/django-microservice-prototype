from django.urls import path
from .views import GetAllOrder

urlpatterns = [
    path('get-all-order/', GetAllOrder.as_view(), name='get-all-orders'),
]