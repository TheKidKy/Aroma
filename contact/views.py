from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm
from .models import Contact

class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        new_msg = Contact(name=name, subject=subject, email=email, message=message)
        new_msg.save()

        return super().form_valid(form)

