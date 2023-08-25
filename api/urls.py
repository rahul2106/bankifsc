# bankdetails/urls.py
from django.urls import path
from .views import BankListAPIView, BankDetailAPIView

urlpatterns = [
    path('ifsc/', BankListAPIView.as_view(), name='ifsc-list'),
    path('ifsc/<str:ifsc>/', BankDetailAPIView.as_view(), name='ifsc-detail'),
]
