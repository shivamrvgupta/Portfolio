from django.contrib import admin
from . import models
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'name',
                    'email', 'phone', 'is_published')
    list_display_links = ('id', 'name', 'job_title')
    list_filter = ('job_title',)
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(models.Job, JobAdmin)
