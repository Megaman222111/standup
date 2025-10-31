from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views import generic
from .forms import EditProfileForm, SignUpForm, EditTimingsForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'index2.html')

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user

class EditTimingsView(generic.UpdateView):
    form_class = EditTimingsForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_timings.html'
    
    def get_object(self):
        return self.request.user.profile

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('login')

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request, *args, **argv):
    return render(request, '500.html')