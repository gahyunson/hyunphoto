from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    pass

# class UserManager(BaseUserManager):
#     use_in_migrations = True 

#     def create_user(self, email, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email
#         user = self.model(email=email, **extra_fields)
#         user.set_password(None)
#         user.save()
#         return user 

#     def create_superuser(self, email, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True')
#         return self.create_user(email, **extra_fields)

# class User(AbstractUser):
#     username = models.CharField(max_length=50, verbose_name='username')
#     email = models.EmailField(unique=True)
#     company = models.CharField(max_length=100, blank=True, null=True)
#     address = models.TextField(max_length=200, blank=True, null=True)
#     address2 = models.TextField(max_length=200, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     nation = models.CharField(max_length=100, blank=True, null=True)
#     postal = models.CharField(max_length=30, blank=True, null=True)
#     phone = models.CharField(max_length=16, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = UserManager()

#     def __str__(self) -> str:
#         return self.email