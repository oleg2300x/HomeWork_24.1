# Generated by Django 4.2.7 on 2024-02-18 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_lesson_course'),
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.course', verbose_name='Оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.lesson', verbose_name='Оплаченный урок'),
        ),
    ]