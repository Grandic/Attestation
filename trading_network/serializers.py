from rest_framework import serializers
from trading_network.models import Link


class NetworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ['debt_to_supplier']