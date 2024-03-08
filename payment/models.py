from django.db import models

from materials.models import Course, Lesson, NULLABLE
from users.models import User


class Payment(models.Model):
    METHODS = (
        ("C", "Cash"),
        ("T", "Translation")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date = models.DateField(verbose_name="Дата платежа")
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name="Оплаченный курс")
    lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.SET_NULL, verbose_name="Оплаченный урок")
    amount = models.PositiveIntegerField(verbose_name="Сумма платежа")
    method = models.CharField(max_length=1, choices=METHODS)

    def __str__(self):
        return f'{self.user}->{self.course}, {self.lesson}, {self.method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


