from rest_framework import generics
from django.db.models import Q, Count
from .models import Bank
from .serializers import BankSerializer, BankNameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

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

        query_params = self.request.query_params
        bank_name = query_params.get('bank_name')
        state = query_params.get('state')
        city = query_params.get('city')
    
        if city:
            queryset = Bank.objects.filter(bank_name=bank_name, state=state, city1=city)
            queryset = queryset.values('branch').annotate(total=Count('branch'))
        elif state:
            queryset = Bank.objects.filter(bank_name=bank_name, state=state)
            queryset = queryset.values('city1').annotate(total=Count('city1'))
        elif bank_name:
            queryset = Bank.objects.filter(bank_name=bank_name)
            queryset = queryset.values('state').annotate(total=Count('state'))
        else:
            queryset = Bank.objects.values('bank_name').annotate(total=Count('bank_name'))
        return queryset


class CustomBankRetrieveAPIView(APIView):

    def get(self, request, *args, **kwargs):
        bank_name = request.query_params.get('bank_name')
        state = request.query_params.get('state')
        city = request.query_params.get('city')
        branch = request.query_params.get('branch')

        try:
            bank = Bank.objects.get(
                bank_name=bank_name,
                state=state,
                city1=city,
                branch=branch
            )
        except Bank.DoesNotExist:
            return Response({'detail': 'Bank not found'}, status=404)

        serializer = BankSerializer(bank)
        data = serializer.data

        response_data = {
            'id': data['id'],
            'bank_name': bank_name,
            'state': state,
            'city': city,
            'branch': branch,
            'ifsc': data['ifsc'],
            'address': data['address'],
            'std_code': data['std_code'],
            'phone': data['phone']

        }

        return Response(response_data)