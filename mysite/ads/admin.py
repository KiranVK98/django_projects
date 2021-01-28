from django.contrib import admin

# Register your models here.
from ads.models import Ad

# Register your models here.

# We want the admin UI to leave the picture and content_type alone


# Define the PicAdmin class
class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad, PicAdmin)