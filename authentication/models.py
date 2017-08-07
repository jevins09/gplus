from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.

class Account(AbstractBaseUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)        #Blank=True makes the fields first and last name optional to be entered by users
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)          #This will also be displayed on user's profile

    is_admin = models.BooleanField(default=False)

    #auto_now_add=True tell django that this field should be automatically set when object is created.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #class AccountManager needs to be created for this which would be created in the next step.
    objects = AccountManager()

    USERNAME_FIELD = 'email'        #This enables the users to login with their email
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


