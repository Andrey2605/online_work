# Generated by Django 5.1.7 on 2025-03-29 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_lesson_course"),
        ("users", "0004_payments_delete_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="course_paid",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите оплаченный курс",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments_course",
                to="materials.course",
                verbose_name="Оплаченный курс",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="lesson_paid",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите оплаченный урок",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments_lesson",
                to="materials.lesson",
                verbose_name="Оплаченный урок",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_amount",
            field=models.PositiveIntegerField(
                blank=True,
                default=0,
                help_text="Укажите сумму оплаты",
                null=True,
                verbose_name="Сумма оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_date",
            field=models.DateTimeField(
                blank=True,
                help_text="Укажите дату оплаты",
                null=True,
                verbose_name="Дата оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_method",
            field=models.CharField(
                blank=True,
                choices=[("cash", "наличные"), ("transfer", "перевод на счет")],
                default="daily",
                help_text="Выберите способ оплаты",
                max_length=255,
                null=True,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
