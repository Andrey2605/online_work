# Generated by Django 5.1.7 on 2025-03-27 12:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_lesson_course"),
        ("users", "0002_payment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="cost",
            new_name="price",
        ),
        migrations.AlterField(
            model_name="payment",
            name="course_paid",
            field=models.ForeignKey(
                help_text="Укажите курс, который покупаете",
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="Приобретенный курс",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="lesson_paid",
            field=models.ForeignKey(
                help_text="Укажите урок, который покупаете",
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lesson",
                verbose_name="Приобретенный урок",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                help_text="Укажите пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
