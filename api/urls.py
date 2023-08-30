# bankdetails/urls.py
from django.urls import path
from .views import BankListAPIView, BankDetailAPIView, BanksListAPIView, CustomBankRetrieveAPIView

urlpatterns = [
    path('ifsc/', BankListAPIView.as_view(), name='ifsc-list'),
    path('ifsc/<str:ifsc>/', BankDetailAPIView.as_view(), name='ifsc-detail'),
    path('banks/', BanksListAPIView.as_view(), name='bank-list'),
    path('detail-view/', CustomBankRetrieveAPIView.as_view(), name='detail-view'),
]
