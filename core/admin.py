from django.contrib import admin

from .models import CustomUser, LeadershipTeam, Event

admin.site.register(CustomUser) 
admin.site.register(LeadershipTeam)

admin.site.register(Event)
