from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# custom user manger
class CustomUserManger(UserManager):
    # function for creating users
    def _create_user(self, email, password, **extra_fields):
        # check if the user provided email address
        if not email:
            raise ValueError("Enter a vaild email address")
        
        # clean email data
        email = self.normalize_email(email)

        # create a user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # set some default values if it's a regular user 
    # and another default fields if it's a superuser
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    

# set the database model
class User(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(blank=True, unique=True, default="")
    name = models.CharField(max_length=255, blank=True, default="")

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    data_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManger()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
"""
a dummy superuser instead of admin *will be removed later 
E: mina@gmail.com
p: Mina12345
"""