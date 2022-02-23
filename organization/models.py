from django.contrib.auth.models import User
from django.contrib.auth.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Unit(models.Model):
    employees = models.ManyToManyField("Employee", blank=True)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    # The GenericForeignKey for demonstration purposes. So the functionality
    # may seem kind of random
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, blank=True, null=True
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    some_object = GenericForeignKey()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
