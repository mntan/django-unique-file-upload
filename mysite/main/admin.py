from django.contrib import admin

from .models import UploadFile


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')    

admin.site.register(UploadFile, FileAdmin)
