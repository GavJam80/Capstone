from django import forms
from .models import CollaborateRequest, AboutPage
from django_summernote.widgets import SummernoteWidget

# Define a form class for users to request a collaboration
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


# Define a form class for the AboutPage model
class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }