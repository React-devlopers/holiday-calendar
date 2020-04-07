from django.contrib import admin

from rest.models import Holiday


class HolidayAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')


admin.site.register(Holiday, HolidayAdmin)
