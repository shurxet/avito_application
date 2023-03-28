from django.conf import settings
from django.db import models

from ads.models.ad import Ad


class Comment(models.Model):
    text = models.CharField(
        max_length=1000,
        null=True,
        verbose_name="текст комментария",
        help_text="Оставьте свой комментарий"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор комментария",
        help_text="Введите автора комментария"
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        null=True,
        related_name="comments",
        verbose_name="Объявление",
        help_text="Объявление, к которому относится комментарий"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="Время создания комментария",
        help_text="Выберите время создания комментария"
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)
