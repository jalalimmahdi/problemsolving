from django.contrib import admin
# Register your models here.

#first we import models that we want to have admin panel for them
from .models import metadata1,metadataN

#a form for managing data of metadata1
#we use metadata1 for configs that will refere by FK of other tables
class metadata1Admin(admin.ModelAdmin):
    list_display=['title','type','description']
    list_filter=['type']
    search_fields=['title']

admin.site.register(metadata1,metadata1Admin)
#end of meatadata1

#a form for managing data of metadataN
#we use metadataN for configs that will refere by FK of other tables
class metadataNAdmin(admin.ModelAdmin):
    list_display=['title','type','description']
    list_filter=['type']
    search_fields=['title']

admin.site.register(metadataN,metadataNAdmin)
#end of meatadataN
