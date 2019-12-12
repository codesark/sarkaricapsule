from django.contrib import admin
from .models import Location, City, State, Country

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Location)