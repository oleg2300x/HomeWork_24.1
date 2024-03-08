from payment.views import PaymentListAPIView
from payment.apps import PaymentConfig
from django.urls import path


app_name = PaymentConfig.name

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]