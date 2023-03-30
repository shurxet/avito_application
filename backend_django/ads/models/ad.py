from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Описание товара")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads", verbose_name="Продавец"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания обявления")
    image = models.ImageField(upload_to="ad_images/", null=True, blank=True, verbose_name="Фото товара")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title
