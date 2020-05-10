from django.contrib import admin
# Register your models here.

from .models import metadata1

class metadata1Admin(admin.ModelAdmin):
    list_display=('title','description','type')
    list_filter=['type']

admin.site.register(metadata1,metadata1Admin)
