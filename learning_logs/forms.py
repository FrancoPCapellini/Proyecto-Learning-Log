from django import forms
from .models import Topic, Entry# Model we'll work with 

class TopicForm(forms.ModelForm):
    # ModelForm consist of a nested Meta class telling Django witch model
    # to base the form on and witch fields to include in the form.
    class Meta:
        model = Topic # Build the form from the Topic model. 
        fields = ['text'] # And includes only text field.
        labels = {'text': ''} # Tells Django not to generate a label for the text field.

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # HTML form element such a single-line text box, multi-line text area, or a drop-down list.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # we are customizing the input widget for the field "text" so the ext area will be 80 columns wide insted of the 40 default.
         