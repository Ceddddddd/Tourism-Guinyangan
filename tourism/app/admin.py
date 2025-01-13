from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Resort)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Falls)
admin.site.register(Restaurant)
admin.site.register(CulturalAttraction)
admin.site.register(Festival)
admin.site.register(Event)
admin.site.register(Activity)

@admin.register(Fiesta)
class FiestaAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'patron_saint')
    search_fields = ('name', 'location', 'patron_saint')
    list_filter = ('date',)