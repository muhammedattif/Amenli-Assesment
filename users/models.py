from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
from django.db import transaction
from django.utils.translation import gettext_lazy as _


def get_image_filename(instance, filename):
    id = instance.id
    return "profile_images/%s/%s" % (id, filename)

# this class is for overriding default users manager of django user model
class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, password=None, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise VlaueError('User must have a username')

        user = self.model(
                        email=self.normalize_email(email),
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        is_staff=is_staff,
                        is_superuser=is_superuser,
                        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    @transaction.atomic
    def create_superuser(self, email, username, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff = True,
            is_superuser = True
        )
        user.save(using = self._db)
        return user

# Account Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name = _('Email'))
    first_name = models.CharField(max_length=30, verbose_name = _('First Name'))
    last_name = models.CharField(max_length=30, verbose_name = _('Last Name'))
    username = models.CharField(max_length=30, unique=True, validators=[UnicodeUsernameValidator()], verbose_name = _('Username'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name = _('Date Joined'))
    last_login = models.DateTimeField(auto_now=True, verbose_name = _('Last Login'))
    is_active = models.BooleanField(default=True, verbose_name = _('Active Status'))
    is_staff = models.BooleanField(default=False, verbose_name = _('Staff Status'))

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta(AbstractBaseUser.Meta, PermissionsMixin.Meta):
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @transaction.atomic
    def save(self, created=None, *args, **kwargs):
        super().save(*args, **kwargs)
