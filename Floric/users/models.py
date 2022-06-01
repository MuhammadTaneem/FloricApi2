from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
import datetime


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/user/', default='images/user/account-avatar-profile.png')
    phone = models.CharField(max_length=15, null=False, blank=False, default='enter your contact number')
    date_of_birth = models.DateField(null=False, blank=False, default=datetime.date.today)
    gender = models.CharField(max_length=31, null=False, blank=False, default='male')
    city = models.CharField(max_length=31, null=False, blank=False, default='dhaka')
    address = models.CharField(max_length=1023, null=False, blank=False, default='set your address ')
    objects = CustomUserManager()

    # username = models.CharField(max_length=50, default=None)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        if (self.first_name):
            return self.first_name + " " + self.last_name
        else:
            return self.email
