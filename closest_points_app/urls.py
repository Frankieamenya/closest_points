from django.urls import path

from .views import find_closest_points

urlpatterns = [
    path('find_closest_points/', find_closest_points, name='find_closest_points'),
]
