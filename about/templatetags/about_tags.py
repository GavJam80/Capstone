# filepath: /workspace/Capstone/about/templatetags/about_tags.py
from django import template
from ..models import AboutPage

register = template.Library()

@register.simple_tag
def has_about_page(user):
    return AboutPage.objects.filter(user=user).exists()