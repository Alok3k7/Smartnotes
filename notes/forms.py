from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

class Notesform(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text': 'Write your thought here:'
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title.isalpha():
            raise ValidationError('Title must contain only alphabetic characters and no numbers or special characters.')
        return title
