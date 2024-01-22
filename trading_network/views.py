from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from trading_network.models import Link
from trading_network.permissions import IsActive
from trading_network.serializers import LinkSerializers


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializers
    queryset = Link.objects.all()
    filter_backends = [OrderingFilter]
    filterset_fields = ('country', )
    permission_classes = [IsActive]
