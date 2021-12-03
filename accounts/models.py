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



class customer(models.Model):
    user   = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
class sellerPost(models.Model):
    user  = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    video = models.URLField()
    price = models.CharField(max_length=10)
    tags  = models.CharField(max_length=100)

class serviceProvider(models.Model):
    user  = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    postbyseller = models.ForeignKey(sellerPost,on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_save_user_profile(created,instance,*args,**kwargs):
    print("OKAyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    if created:
        print("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        customer.objects.create(user=instance)