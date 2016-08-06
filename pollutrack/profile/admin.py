from django.contrib import admin

from profile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('owner',)


admin.site.register(Profile, ProfileAdmin)