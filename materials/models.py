from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    img = models.ImageField(upload_to='course', verbose_name='Картинка', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    img = models.ImageField(upload_to='lesson', verbose_name='Картинка', **NULLABLE)
    url = models.URLField(verbose_name='Ссылка на урок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'