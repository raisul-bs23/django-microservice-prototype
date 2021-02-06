from django.urls import path, include

urlpatterns = [
    path('invoice/', include('invoiceapp.urls')),
]
