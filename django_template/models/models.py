from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django_template.managers import CustomUserManager


class TemplateModel(models.Model):
    class Meta:
        abstract = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
