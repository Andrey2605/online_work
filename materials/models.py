from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Укажите название курса"
    )
    image = (
        models.ImageField(
            upload_to="media/images", blank=True, null=True, verbose_name="Превью"
        ),
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название урока", help_text="Укажите название урока"
    )
    image = (
        models.ImageField(
            upload_to="media/images", blank=True, null=True, verbose_name="Превью"
        ),
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Укажите курс",
    )

    video_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Введите URL-адрес видео для урока (необязательно).",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
