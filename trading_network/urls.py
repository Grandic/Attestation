from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trading_network.apps import TradingNetworkConfig
from trading_network.views import LinkViewSet

app_name = TradingNetworkConfig.name

router = DefaultRouter()
router.register(r'trading_network', LinkViewSet, basename='trading_network')


urlpatterns = [
    path('', include(router.urls)),
]