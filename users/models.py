from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
#from mixins import InspectableModel

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('The superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    email = models.EmailField(unique=True)

    username = True

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
