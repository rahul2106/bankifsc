# bankdetails/serializers.py
from rest_framework import serializers
from .models import Bank

class BankNameSerializer(serializers.Serializer):
    bank_name = serializers.CharField()

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
