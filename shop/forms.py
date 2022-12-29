from django import forms
from .models import ProductComment

class comment_model_form(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = '__all__'
        exclude = ['product']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email Address'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Message'
            })
        }

