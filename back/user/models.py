from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField


class User(models.Model):
    USER_TYPE = (
        (1, 'Admin'),
        (2, 'Company'),
        (3, 'Customer')
    )

    REGION = (
        (1, 'Kokshetau'),
        (2, 'Makinsk'),
        (3, 'Burabay')
    )

    name = models.CharField(max_length=150, verbose_name='ФИО')
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
    telephone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=75, verbose_name='Адрес')
    created_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(unique=True, verbose_name='Почта')
    city = MultiSelectField(choices=REGION, verbose_name='Город')
    username = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
