# Generated by Django 3.2 on 2023-03-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Адрес электронной почты')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=5, verbose_name='Права доступа')),
                ('image', models.ImageField(null=True, upload_to='user_avatars/', verbose_name='Фото пользователя')),
                ('is_active', models.BooleanField(verbose_name='Активен ли пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users_user',
            },
        ),
    ]
