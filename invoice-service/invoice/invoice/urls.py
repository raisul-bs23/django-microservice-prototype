from django.urls import path, include

urlpatterns = [
    path('', include('invoiceapp.urls')),
]
