from django.contrib import admin

from event.models import Event, Freebie


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('slogan', 'owner',)


admin.site.register(Event, EventAdmin)
admin.site.register(Freebie)
