from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from users.serializers import PaymentSerializer
from users.models import Payment
from django_filters.rest_framework import DjangoFilterBackend


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lesson", "method")
    ordering_fields = ("date",)
