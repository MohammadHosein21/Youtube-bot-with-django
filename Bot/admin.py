from django.contrib import admin
from .models import Channel
from django.db.models.functions import Lower


# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'subscriber', 'link', 'keyword']
    list_filter = ['keyword']
    ordering = ['-subscriber']
