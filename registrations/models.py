from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if 'role' in kwargs:
            role = kwargs.pop('role')
        else:
            role = self.model.base_role
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)
        user.role = role

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_admin(self, email,first_name,last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,  # Pass first_name to create_user
            last_name=last_name
        )
        user.is_admin = True
        user.role = User.Role.ADMIN
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('role', 'ADMIN')  # Set role explicitly to 'ADMIN'

        if kwargs.get('role') != 'ADMIN':
            raise ValueError('Superuser must have role set to ADMIN.')

        return self.create_user(email, password, **kwargs)

class StudentManager(AccountManager):
    def create_student(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,  # Pass first_name to create_user
            last_name=last_name
        )
        user.is_student = True
        user.role = User.Role.STUDENT  # Set role to 'STUDENT'
        user.save(using=self._db)
        return user

class AlumniManager(AccountManager):
    def create_alumni(self, email, first_name,last_name,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,  # Pass first_name to create_user
            last_name=last_name
        )
        user.is_alumni = True
        user.role = User.Role.ALUMNI  # Set role to 'ALUMNI'
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        ALUMNI = "ALUMNI", "Alumni"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.role:  # If role is not set, set it to base_role
            self.role = self.base_role
        return super().save(*args, **kwargs)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class Student(User):
    class Meta:
        proxy = True
    base_role = User.Role.STUDENT
    objects = StudentManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_student = True
        super().save(*args, **kwargs)

class Alumni(User):
    class Meta:
        proxy = True
    base_role = User.Role.ALUMNI
    objects = AlumniManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_alumni = True
        super().save(*args, **kwargs)