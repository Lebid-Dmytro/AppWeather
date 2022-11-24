from django.contrib import admin
from django.utils.html import format_html

from weather import models

# admin.site.register(City)
# admin.site.register(About)


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass
