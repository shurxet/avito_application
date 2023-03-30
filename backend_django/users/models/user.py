from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from users.managers import UserManager


# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        USER = "user", "Пользователь"

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(unique=True, max_length=50, verbose_name="Адрес электронной почты")
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER, verbose_name="Права доступа")
    image = models.ImageField(upload_to='user_avatars/', null=True, verbose_name="Фото пользователя")
    is_active = models.BooleanField(verbose_name="Активен ли пользователь")


    class Meta(object):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        app_label = 'users'
        db_table = 'users_user'

    @property
    def is_admin(self):
        return self.role == User.Role.ADMIN

    @property
    def is_user(self):
        return self.role == User.Role.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email
