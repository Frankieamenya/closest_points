from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Point

@api_view(['POST'])
def find_closest_points(request):
    coordinates = request.data.get('points', '')
    point = Point(coordinates=coordinates)
    point.save()

    points = coordinates.split(';')

    x_values = []
    y_values = []

    for point in points:
        x, y = map(int, point.split(','))
        x_values.append(x)
        y_values.append(y)

    min_distance = float('inf')
    closest_points = []

    for i in range(len(points)):
        x1 = x_values[i]
        y1 = y_values[i]

        for j in range(i + 1, len(points)):
            x2 = x_values[j]
            y2 = y_values[j]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            if distance < min_distance:
                min_distance = distance
                closest_points = [(x1, y1), (x2, y2)]

    return JsonResponse({'closest_points': closest_points})
