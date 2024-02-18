from users.views import PaymentListAPIView
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from django.urls import path


app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]