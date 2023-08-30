from random import choices
from django import forms
from django.core.validators import ValidationError
from blog.models import Message


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label='your name')
    text = forms.CharField(max_length=1000, label='your massage')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code='name_text_same')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
