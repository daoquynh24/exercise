# Python imports

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True


class BaseAbstractUser(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True

    objects = AbstractBaseUser()


class AbstractUser(BaseModel):
    REQUIRED_FIELDS = ('phone',)
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

    class Meta:
        abstract = True


