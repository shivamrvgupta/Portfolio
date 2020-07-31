from django.db import models
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField(max_length=40)
    description = models.TextField(blank=True)
    place = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        print("Blog is published")
        return self.title
