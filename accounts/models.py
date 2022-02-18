from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

# create a custom super user class
class AccountManager(BaseUserManager):

    # create user method
    def create_user(self,first_name, last_name, email, username, password=None):
        
        # check if user exists
        if not email:
            raise ValueError('User must have an email address.')
        
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            email=self.normalize_email(email),
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=50)

    # define the required fields
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # cheange login action from username to email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # tell the class that we are using the Accounts manager class to perform all user operations
    objects = AccountManager()

    def __str__(self) -> str:
        return self.email

    # permissions methods
    def has_perm(self, perm, abj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True