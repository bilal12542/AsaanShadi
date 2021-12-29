from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from io import BytesIO
from PIL import Image
from django.core.files import File


# Create your models here.


def get_image_filename(instance, filename):
    product = instance.product_id.id
    title = instance.product_id.title
    slug = slugify(title)
    return "productImg/%s-%s-%s" % (product, slug, filename)


def get_thumbnail_filename(instance, filename):
    product = instance.id
    title = instance.title
    slug = slugify(title)
    return "productImg/%s-%s-%s-thumbnail" % (product, slug, filename)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    owner_name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=60)
    tagline = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner_name


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    tags = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1000, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to=get_thumbnail_filename, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=get_thumbnail_filename, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(240, 180)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Images(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')

