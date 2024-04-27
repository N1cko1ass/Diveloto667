from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm, AuthorizationForm


def index(request):
    return render(request, 'index.html')


class registration(CreateView):
    form_class = SignUpForm
    template_name = 'SignUp.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class authorization(LoginView):
    form_class = AuthorizationForm
    template_name = 'SignIn.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def profile_main(request):
    return render(request, 'profile/main-info.html')


def profile_notifications(request):
    return render(request, "profile/main-profile-notifications.html")


def profile_bonuses(request):
    return render(request, "profile/main-profile-bonuses.html")
