from django.db import models
from datetime import datetime

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    body = models.TextField(max_length=200, blank=True)
    summary = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    job_title = models.CharField(max_length=25)
    is_published = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=datetime.now, blank=False)
    end_date = models.DateTimeField(default=datetime.now, blank=False)
    address = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=25)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
