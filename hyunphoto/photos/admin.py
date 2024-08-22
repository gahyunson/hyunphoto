from django.contrib import admin
from .models import Photo, Price

class PhotoAdmin(admin.ModelAdmin):
    pass
class PriceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Price, PriceAdmin)
