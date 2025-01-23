from django import forms
from .models import CollaborateRequest, AboutPage
from django_summernote.widgets import SummernoteWidget

# Define a form class for users to request response for more info
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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


# Define a form class for the AboutPage model
class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }