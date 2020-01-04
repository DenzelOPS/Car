from django.db import models

class Car_test(models.Model):
    car_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='car_id')
    color = models.CharField(max_length=50, blank=True)
    year = models.IntegerField(blank=True)
    manufacturer = models.CharField(max_length=50, blank=True)
