from django.db import models
from accounts.models import CustomUser
# Create your models here.
class sellerPost(models.Model):
    user  = models.ForeignKey("accounts.ServiceProvider",on_delete=models.CASCADE,verbose_name="custom user")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(default=" ",upload_to='media/images/sellerpost')
    video = models.URLField()
    price = models.PositiveIntegerField() # limit the price in future
    tags  = models.CharField(max_length=100)
