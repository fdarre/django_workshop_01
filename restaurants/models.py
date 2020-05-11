#from django.db import models
from django.contrib.gis.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    # PointField is provided by Geodjango
    # it represents the coordinates of the point (longitude and latitude)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.pk})
