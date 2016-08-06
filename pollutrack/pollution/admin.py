from django.contrib import admin
from pollution.models import Coordinates, PollutionSource, Victim, Disease

# Register your models here.
admin.site.register(Coordinates)
admin.site.register(PollutionSource)
admin.site.register(Victim)
admin.site.register(Disease)
