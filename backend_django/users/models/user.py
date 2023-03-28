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
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    role = models.CharField(max_length=5, choices=Role.choices, default=Role.USER)
    image = models.ImageField(upload_to='user_avatars/', null=True)


    # email = models.CharField(
    #     max_length=100,
    #     default="email_address",
    #     unique=True,
    #     help_text="Введите электронную почту",
    #     null=True
    # )
    # phone = PhoneNumberField(
    #     verbose_name="Номер телефона",
    #     help_text="Укажите номер телефона",
    #     null=True
    #     #blank=True
    # )
    #
    # role = models.CharField(
    #     max_length=5,
    #     choices=ROLES,
    #     default=USER,
    #     verbose_name="Роль пользователя",
    #     help_text="Укажите роль"
    # )
    # first_name = models.CharField(
    #     max_length=50,
    #     verbose_name="Имя",
    #     help_text="Введите имя(максимум 50 символов)",
    #     default="first_name",
    #     null=True
    # )
    # last_name = models.CharField(
    #     max_length=50,
    #     verbose_name="Фамилия",
    #     help_text="Введите фамилию(максимум 50 символов)",
    #     default="last_name",
    #     null=True
    # )
    # is_active = models.BooleanField(
    #     default=False, verbose_name="Аккаунт активен",
    #     help_text="Укажите активен ли аккаунт",
    #     null=True
    # )
    # image = models.ImageField(
    #     upload_to='users_avatars/',
    #     null=True,
    #     blank=True,
    #     verbose_name="Аватарка",
    #     help_text="Выбери свой аватар"
    # )
    #
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
