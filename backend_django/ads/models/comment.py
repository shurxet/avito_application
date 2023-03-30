from django.conf import settings
from django.db import models

from ads.models.ad import Ad


class Comment(models.Model):
    text = models.TextField(null=False, blank=False, verbose_name="Текст")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", verbose_name="Автор"
    )
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments", verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
