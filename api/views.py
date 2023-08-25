# bankdetails/views.py
from rest_framework import generics
from .models import Bank
from .serializers import BankSerializer


class BankListAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetailAPIView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'ifsc'
