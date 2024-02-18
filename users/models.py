from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='Фото')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

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
        verbose_name = 'Платежь'
        verbose_name_plural = 'Платежи'

