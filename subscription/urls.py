from django.urls import path

from subscription.apps import SubscriptionConfig
from subscription.views import SubscribeAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscriptions/', SubscribeAPIView.as_view(), name='subscriptions'),
]