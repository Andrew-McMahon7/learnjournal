from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()


class JournalResource(models.Model):
    journalName = models.CharField(max_length=200)
    journalUrl = models.URLField()
    lastAccessed = models.DateTimeField()
    tagIds = models.JSONField(blank = True)


class TagsResource(models.Model):
    tagName = models.CharField(max_length=200)
    tagUrl = models.URLField()
    imageUrl = models.URLField(blank = True)


class ContactsResource(models.Model):
    contactName = models.CharField(max_length=200)
    contactEmail = models.EmailField(blank = True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contactNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
