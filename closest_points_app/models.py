from django.db import models

class Point(models.Model):
    coordinates = models.CharField(max_length=255)
    closest_points = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.coordinates
    
    class Meta:
        app_label = 'closest_points_app'

