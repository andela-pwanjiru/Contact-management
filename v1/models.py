from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contacts(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Person(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
