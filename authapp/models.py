from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Класс модели пользователя
    """
    username = models.CharField("username", max_length=150,
                                null=True, blank=True)
    middle_name = models.CharField("middle name",
                                   max_length=150,
                                   blank=True)
    email = models.EmailField("email address",
                              unique=True)  # переопределение

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.first_name + ' ' + self.last_name
