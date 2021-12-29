from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Package(models.Model):
    package = models.CharField(max_length=100, default="", unique = True)
    price = models.CharField(max_length=130 , default="")

    def __str__(self):
        return self.package


class Category(models.Model):
    category = models.CharField(max_length=250,unique = True )


    def __str__(self):
        return self.category

class ServiceProvider(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150, default="")
    contact_no = models.CharField(max_length=100 , default="")
    desc = models.TextField()
    package = models.ForeignKey(Package,  on_delete=models.CASCADE )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", default="")


    def __str__(self):
        return self.company_name

class Become_ServiceProvider(models.Model):
    owner_name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=60)
    tagline = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='ServiceProvider', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner_name


