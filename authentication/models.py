from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

'''
When substituting a custom user model, it is required that you also define a related Manager class that overrides the
create_user() and create_superuser() methods.
'''
class AccountManager(BaseUserManager):

    #This method creates a new user and returns error if any appropriately.
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')


        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):

        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account

class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)        #Blank=True makes the fields first and last name optional to be entered by users
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)          #This will also be displayed on user's profile


    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text=('Designates whether the user can log into this admin site')
                                   )
    is_active = models.BooleanField(('active'), default=True,
                                    help_text = ('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
                                    )

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


