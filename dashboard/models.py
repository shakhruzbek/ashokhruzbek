from django.db import models

# Create your models here.
POSITIONS = (
    ('administrator', 'Administrator'),
    ('staff', 'Ishchi'),
    ('ceo', 'Boshliq'),
)

class Company(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    telegram = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField()

class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(blank=True, null=True, max_length=20)
    position = models.CharField(choices=POSITIONS, max_length=13)
    short_description = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="staff/")


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.IntegerField()