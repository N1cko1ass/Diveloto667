from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class registration(CreateView):
    form_class = SignUpForm
    template_name = 'main/SignUp.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    # def SignUp(request):
    #     if request.method == 'POST':
    #             form = SignUpForm(request.POST)
    #             if form.is_valid():
    #                 user = form.save()
    #                 send_confirmation_email(user)  # Отправляем подтверждающее письмо
    #                 return HttpResponseRedirect('home')  # Замените 'home' на имя вашего URL для перенаправления после регистрации
    #             else:
    #                 form = SignUpForm()
    #             return render(request, 'main/SignUp.html', {'form': form})

    #     def send_confirmation_email(user):
    #         subject = 'Welcome to Our Site'
    #         message = f'Hi {user.username}, thank you for registering with us.'
    #         from_email = 'diveloto@mail.ru'  # Ваша почта для отправки писем
    #         to_email = user.email
    #         send_mail(subject, message, from_email, [to_email])


class authorization(LoginView):
    form_class = AuthorizationForm
    template_name = 'main/SignIn.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('authorization')


def profile_main(request):
    return render(request, 'main/profile/main-info.html')


def profile_notifications(request):
    return render(request, "main/profile/main-profile-notifications.html")


def profile_bonuses(request):
    return render(request, "main/profile/main-profile-bonuses.html")