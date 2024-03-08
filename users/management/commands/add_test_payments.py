from django.core.management import BaseCommand

from payment.models import Payment

test_payments = [
    {
        "user_id": 1,
        "date": "2023-01-23",
        "course_id": 1,
        "amount": 10000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-24",
        "course_id": 1,
        "amount": 20000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-03",
        "lesson_id": 1,
        "amount": 10000,
        "method": "C",
    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for test_payment in test_payments:
            payment = Payment.objects.create(**test_payment)
            payment.save()
        print(payment)
