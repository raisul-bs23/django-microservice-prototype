from django.urls import path, include

urlpatterns = [
    path('order/', include('orderapp.urls')),
]