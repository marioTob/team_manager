from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    position = models.CharField(max_length=50, null=False, blank=False)
    hire_date = models.DateField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
