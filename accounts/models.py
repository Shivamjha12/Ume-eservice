from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from accounts.managers import CustomUserManager
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
# Create your models here.ff
from django.db.models import Q
# from ume.models import 


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email adress'),unique=True)
    # phone_no = models.IntegerField(('phone'),unique=True,default="Null")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)

    is_customer = models.BooleanField(default=True)
    is_serviceProvider = models.BooleanField(default=False)
    is_serviceBusiness = models.BooleanField(default=False)


    fields=[email]
    USERNAME_FIELD = 'email'
    EMAIL_FIELD=['email']
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()



    class Types(models.TextChoices):
        SELLER = "Seller", "SELLER"
        CUSTOMER = "Customer", "CUSTOMER"
        
    default_type = Types.CUSTOMER
    type = MultiSelectField(choices=Types.choices, default=[], null=True, blank=True)



    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.id:
            #self.type = self.default_type
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)


class serviceProviderDetails(models.Model):
    user  = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(default=" ",max_length=20)
    last_name = models.CharField(default=" ",max_length=20)
    your_Address = models.CharField(default=" ",max_length=150)
    langitude_loc = models.IntegerField(default=0)
    longitude_loc = models.IntegerField(default=0)
    adharcard = models.ImageField(default=" ",upload_to='media/images/adharcard')
    # postbyseller = models.ForeignKey(sellerPost,on_delete=models.CASCADE,null=True, blank=True)

    
class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.SELLER))

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.CUSTOMER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.CUSTOMER))

class ServiceProvider(CustomUser):
    default_type= CustomUser.Types.SELLER
    object = SellerManager()
    class Meta:
        proxy = True
    
    def sell():
        print("Seller can sell")
    @property
    def showAditional(self):
        return self.serviceProvider

class customer(CustomUser):
    default_type= CustomUser.Types.CUSTOMER
    object = CustomerManager()
    class Meta:
        proxy = True
    def buy():
        print("buyer can buy")
    @property
    def showAditional(self):
        return self.customer




# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_or_save_user_profile(created,instance,*args,**kwargs):
#     print("OKAyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
#     if created:
#         print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
#         customer.objects.create(user=instance)