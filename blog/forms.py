from django import forms


class PostCommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Name'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter Email Address'})
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'subject', 'placeholder': 'Subject'})
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control mb-10', 'placeholder': 'Message'})
    )
