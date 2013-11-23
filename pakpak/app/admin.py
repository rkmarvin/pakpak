from django.contrib import admin
from app.models import Sound


class SoundAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


admin.site.register(Sound, SoundAdmin)
1 / 0
