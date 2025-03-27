from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
    )
    city = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(upload_to="users/avatars", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"