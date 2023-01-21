from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import RegisterForm

user = get_user_model()

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'user/register.html', context={'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('full_name')
            password = register_form.cleaned_data.get('password')
            email = register_form.cleaned_data.get('email')

        user_exist: bool = user.objects.filter(email=email).exists()
        if user_exist:
            register_form.add_error('email', 'this email is used by another user')
        else:
            new_user = user(username=username, password=password, email=email)
            new_user.set_password(password)
            new_user.save()

        return render(request, 'user/register.html', context={'register_form': register_form})
