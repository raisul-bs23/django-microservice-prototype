from django.urls import path
from .views import GetAllInvoice

urlpatterns = [
    path('get-all-invoice/', GetAllInvoice.as_view(), name='get-all-invoice'),
]
