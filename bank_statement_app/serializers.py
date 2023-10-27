from rest_framework import serializers

class BankStatementSerializer(serializers.Serializer):
    month = serializers.CharField(max_length=50)
    transactions = serializers.ListField()
    opening_balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_credit_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_debit_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    closing_balance = serializers.DecimalField(max_digits=10, decimal_places=2)
