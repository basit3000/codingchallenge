from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Event(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.name