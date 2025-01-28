from .models import Comment
from django import forms


# Define a form class for the Comment model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        