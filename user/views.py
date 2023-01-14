from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

user = get_user_model()

class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')
