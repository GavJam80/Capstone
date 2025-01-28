from django.contrib import admin
from .models import About, CollaborateRequest, AboutPage
from django_summernote.admin import SummernoteModelAdmin


# Register the About model with the admin site using the SummernoteModelAdmin
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    # Specify which fields should use the Summernote editor
    summernote_fields = ('content',)

# Register the CollaborateRequest
# model with the admin site using the default ModelAdmin


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    # Specify which fields should be displayed in the list view
    list_display = ('message', 'read',)

# Register the AboutPage model with the
# admin site using the SummernoteModelAdmin


@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    # Specify which fields should be displayed in the list view
    list_display = ('user', 'content')
    # Add search functionality for the specified fields
    search_fields = ('user__username', 'content')
    # Specify which fields should use the Summernote editor
    summernote_fields = ('content',)
    