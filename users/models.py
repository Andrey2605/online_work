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


class Payments(models.Model):
    from materials.models import Course, Lesson
    PAYMENT_METHOD = (
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Плательщик",
        help_text="Укажите плательщика",
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты",
        help_text="Укажите дату оплаты",
        blank=True,
        null=True,
    )
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="payments_course",
        verbose_name="Оплаченный курс",
        help_text="Укажите оплаченный курс",
        blank=True,
        null=True,
    )
    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="payments_lesson",
        verbose_name="Оплаченный урок",
        help_text="Укажите оплаченный урок",
        blank=True,
        null=True,
    )
    payment_amount = models.PositiveIntegerField(
        default=0,
        verbose_name="Сумма оплаты",
        help_text="Укажите сумму оплаты",
        blank=True,
        null=True,
    )
    payment_method = models.CharField(
        choices=PAYMENT_METHOD,
        max_length=255,
        default="daily",
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
        blank=True,
        null=True,
    )
