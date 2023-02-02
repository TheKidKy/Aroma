from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.urls import reverse

from .forms import RegisterForm, LoginForm

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
            elif len(password) < 8:
                register_form.add_error('password', 'this password is too short')
            else:
                new_user = user(username=username, password=password, email=email)
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse('login-page'))

        return render(request, 'user/register.html', context={'register_form': register_form})


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'user/login.html', context={'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            current_user: user = user.objects.filter(email__iexact=email).first()
            if current_user is not None:
                is_password_correct = current_user.check_password(password)
                if is_password_correct:
                    login(request, current_user)
                    return redirect(reverse('home-page'))
                else:
                    login_form.add_error('password', 'The entered password is incorrect')
            else:
                login_form.add_error('email', 'No user was found with this information')

        return render(request, 'user/login.html', context={'login_form': login_form})


