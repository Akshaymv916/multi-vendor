from django.urls import path
from .views import VendorRegisterView, VendorProfileView

urlpatterns = [
    path('register/', VendorRegisterView.as_view(), name='vendor-register'),
    path('profile/', VendorProfileView.as_view(), name='vendor-profile'),
]
