from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название товара",
        help_text="Введите название товара"
    )
    price = models.PositiveIntegerField(
        null=True, verbose_name="Цена",
        help_text="Укажите цену на товар"
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name="Описание товара",
        help_text="Введите описание товара"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name="Автор объявления",
        help_text="Введите автора объявления"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания объявления",
        help_text="Выберите время создания объявления"
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото",
        help_text="Разместите фото для объявления",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)
