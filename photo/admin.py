from django.contrib import admin
from .models import Photo

# Register your models here.
from django.contrib import admin


# Register your models here.
from .models import Photo, User


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(User)

