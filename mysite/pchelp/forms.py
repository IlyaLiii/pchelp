from django.forms import ModelForm
from .models import Feedback
from django import forms

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('first_name','email','item','problem')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Имя:'}),
            'email': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Почта или телефон:'}),
            'item': forms.TextInput(attrs={'class':'form-control','placeholder':'С чем проблема?'}),
            'problem': forms.TextInput(attrs={'class':'form-control','placeholder':'Опишите проблему:'}),
        }

