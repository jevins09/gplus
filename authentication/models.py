from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class AccountManager(BaseUserManager):

    #This method creates a new user and returns error if any appropriately.
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        '''
        Since we haven't defined a model attribute on the AccountManager class,
        self.model refers to the model attribute of BaseUserManager. This defaults
        to settings.AUTH_USER_MODEL, which we will change in just a moment to
        point to the Account class.
        '''

        '''
        account = self.model(
            email = self.normalize_email(email), username=kwargs.get('username')
        )
        '''

        account = self.create_account(email, password, **kwargs)

        account.is_admin = True

        #account.set_password(password)
        account.save()

        return account

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


