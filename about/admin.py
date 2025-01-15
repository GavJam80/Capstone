from django.contrib import admin
from .models import About, CollaborateRequest, AboutPage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)

@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    list_display = ('user', 'content')
    search_fields = ('user__username', 'content')
    summernote_fields = ('content',)