from django.contrib import admin
from . import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'zipcode', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('place',)
    list_editable = ('is_published',)
    search_fields = ('title', 'body', 'place', 'state', 'zipcode')
    list_per_page = 25
admin.site.register(models.Blog, BlogAdmin)
