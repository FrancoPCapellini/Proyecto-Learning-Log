from django import forms
from .models import Topic # Model we'll work with 

class TopicForm(forms.ModelForm):
    # ModelForm consist of a nested Meta class telling Django witch model
    # to base the form on and witch fields to include in the form.
    class Meta:
        model = Topic # Build the form from the Topic model. 
        fields = ['text'] # And includes only text field.
        labels = {'text': ''} # Tells Django not to generate a label for the text field.