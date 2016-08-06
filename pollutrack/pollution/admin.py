from django.contrib import admin
from pollution.models import Coordinates, PollutionSource


class PollutionAdmin(admin.ModelAdmin):
    model = PollutionSource
    list_display = ('address', 'owner',)


admin.site.register(Coordinates)
admin.site.register(PollutionSource, PollutionAdmin)
