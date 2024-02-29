from rest_framework import serializers

from subscription.models import Subscriptions


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'