from django.db import models

from materials.models import Course
from users.models import User


class Subscriptions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
