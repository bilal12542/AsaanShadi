from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Catering(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150, default="")
    contact_no = models.CharField(max_length=100 , default="")
    desc = models.CharField(max_length=400 ,  default="")
    package = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=130 , default="")

    def __str__(self):
        return self.company_name


class Decoration(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150, default="")
    contact_no = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=400, default="")
    package = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=130, default="")

    def __str__(self):
        return self.company_name

class Transportation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150, default="")
    contact_no = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=400, default="")
    package = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=130, default="")

    def __str__(self):
        return self.company_name


class Photography(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150, default="")
    contact_no = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=400, default="")
    package = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=130, default="")

    def __str__(self):
        return self.company_name



