from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
# Python imports

# Django imports
from datetime import timedelta

import jwt
from django.db import models
from django.utils.datetime_safe import datetime

from api import settings
from base.models import AbstractUser
from base.constants.common import AppConstants


# Create your models here.
class User(AbstractUser):
    # Base user already have: first_name, last_name, email, ...
    email = models.CharField(unique=True, max_length=200)
    phone = models.CharField(null=True, max_length=20, unique=True)
    role_id = models.PositiveSmallIntegerField(default=AppConstants.Role.USER)
    is_email_confirmed = models.BooleanField(default=False)
    confirm_email_key = models.CharField(max_length=100, null=True)
    reset_password_key = models.CharField(max_length=100, null=True)
    reset_password_expired_at = models.DateTimeField(null=True, default=None)
    avatar = models.CharField(max_length=200, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    object = AbstractUser()

#     def __str__(self):
#         return self.email
#
#     @property
#     def token(self):
#         return self._generate_jwt_token()
#
#     def _generate_jwt_token(self):
#         dt = datetime.now() + timedelta(days=60)
#
#         token = jwt.encode({
#             'id': self.pk,
#             'exp': int(dt.strftime('%s'))
#         }, settings.SECRET_KEY, algorithm='HS256')
#
#         return token.decode('utf-8')
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#         return user
