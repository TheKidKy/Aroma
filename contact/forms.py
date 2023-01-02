from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'name': 'name',
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'name': 'email',
        'placeholder': 'Enter email address'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'name': 'subject',
        'placeholder': 'Enter Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control different-control w-100',
        'id': 'message',
        'name': 'message',
        'cols': '30',
        'rows': '5',
        'placeholder': 'Enter Message'
    }))
