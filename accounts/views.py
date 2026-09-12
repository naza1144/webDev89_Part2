from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import ProfileForm, RegistrationForm

from .models import Profile
# Create your views here.
def home_view(request):
    context = {}
    if request.user.is_authenticated:
        #ดึงโปรไฟล์
        context['profile'] = Profile.objects.filter(user=request.user).first()
        context['avatar_url'] = context['profile'].avatar.url if context['profile'].avatar else ''
    return render(request, 'accounts/home.html', context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)  # Create a Profile instance for the new user
        return response

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')