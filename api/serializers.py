# bankdetails/serializers.py
from rest_framework import serializers
from .models import Bank

class BankNameSerializer(serializers.Serializer):
    bank_name = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city1 = serializers.CharField(required=False)
    branch = serializers.CharField(required=False)

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
