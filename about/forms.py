from django import forms
from .models import CollaborateRequest, AboutPage
from django_summernote.widgets import SummernoteWidget

class CollaborateForm(forms.ModelForm):
    """
    Form class for users to request a collaboration
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }