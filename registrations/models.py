from django.db import models
from django.conf import settings
from userprofile.models import StudentProfile, AlumniProfile
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email,**kwargs )

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_admin(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    def create_student(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
        )
        user.is_student = True
        user.save(using=self._db)
        return user
    def create_alumni(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
        )
        user.is_alumni = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email,password=password,**kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    is_student = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    
    
    

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email




