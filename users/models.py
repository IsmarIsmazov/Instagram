from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import CustomUseManager






class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model for the Django authentication system.'''
    email = models.EmailField(max_length=25,
                              unique=True,
                              verbose_name="Почта"
                              )
    username = models.CharField(max_length=20,
                                verbose_name="Имя пользователя"
                                )
    phone = PhoneNumberField(max_length=20,
                             blank=True,
                             verbose_name="Номер телефона",
                             )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    objects = CustomUseManager()



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",
                       "phone",
                       ]



    def __str__(self):
        return self.username
















