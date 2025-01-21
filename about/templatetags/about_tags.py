from django import template
from ..models import AboutPage

# Create an instance of the template.Library class to register custom template tags
register = template.Library()

# Register a simple tag named 'has_about_page'
@register.simple_tag
def has_about_page(user):
    # Check if an AboutPage exists for the given user and return True or False
    return AboutPage.objects.filter(user=user).exists()