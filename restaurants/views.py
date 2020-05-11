from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Restaurant

# Coordinates for Lyon (Perrache station) in France
latitude = 45.748554
longitude = 4.825655

# srid = Spatial Reference Identifier
# 4326 corresponds to “longitude/latitude on the WGS84 spheroid”.
target_location = Point(longitude, latitude, srid=4326)

"""
Get the nearby restaurants
Each object is annotated with a distance annotation that’s calculated
between the location of each restaurant and the user’s location given above.
"""


class Homepage(generic.ListView):
    model = Restaurant
    context_object_name = "restaurants"
    queryset = Restaurant.objects.annotate(
        distance=Distance("location", target_location)
    ).order_by("distance")[0:6]
    template_name = "restaurants/home.html"


class RestaurantDetail(DetailView):
    model = Restaurant


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'address', 'city']


class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['name', 'address', 'city']


class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurant-homepage')
