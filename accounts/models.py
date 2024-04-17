from django.contrib.auth.models import User
from django.db import models

from .utils import validate_phone_number


class Profile(models.Model):
    image = models.ImageField(
        upload_to="profile/",
        verbose_name="Фотография",
        help_text="Это поле предназначено для изображения профиля пользователя. Картинка должна быть Х на Х.",
        blank=True,
        null=True
    )

    company_name = models.CharField(
        verbose_name="Наименование компании",
        max_length=255,
        null=True, blank=True
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Поле для хранения номера телефона пользователя. Уникальное, с возможностью валидации.",
        blank=True,
        null=True,
        validators=[validate_phone_number]
    )

    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Поле для хранения даты рождения пользователя.",
        blank=True,
        null=True
    )

    about = models.TextField(
        max_length=200,
        verbose_name="Обо мне",
        help_text="Текстовое поле для краткой информации о пользователе, ограниченное 200 символами.",
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Поле связи 'один к одному' с моделью пользователя Django."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания профиля, автоматически устанавливаемые при создании новой записи."
    )

    def __str__(self) -> str:
        return f"Пользователь: {self.user.username}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["-created_at"]
