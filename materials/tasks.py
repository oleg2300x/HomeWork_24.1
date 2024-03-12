from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from subscription.models import Subscriptions


@shared_task
def send_email_update_course(course):
    subscriptions = Subscriptions.objects.all().filter(course=course)
    users = []
    for subscription in subscriptions:
        users.append(subscription.user)
    for user in users:
        message = f"Здравствуйте {user.name}. {course.name} выл обновлён."
        send_mail(
            subject="Обновление курса",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )