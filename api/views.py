from rest_framework import generics
from django.db.models import Q, Count
from .models import Bank
from .serializers import BankSerializer, BankNameSerializer

class BankListAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        bank_name = query_params.get('bank_name')
        state = query_params.get('state')
        city = query_params.get('city')
        branch = query_params.get('branch')

        queryset = Bank.objects.all()

        if bank_name:
            queryset = queryset.filter(bank_name=bank_name)
        if state:
            queryset = queryset.filter(state=state)
        if city:
            queryset = queryset.filter(Q(city1=city) | Q(city2=city))
        if branch:
            queryset = queryset.filter(branch=branch)

        return queryset

class BankDetailAPIView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'ifsc'


class BanksListAPIView(generics.ListAPIView):
    serializer_class = BankNameSerializer

    def get_queryset(self):
        queryset = Bank.objects.values('bank_name').annotate(total=Count('bank_name'))
        return queryset
