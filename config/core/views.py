from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Vehicle, Driver
from .forms import VehicleForm


class LoginView(LoginView):
    template = 'core/registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'core/vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'core/vehicle_detail.html'

class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'core/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'core/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'core/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')

class RegisterView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form':form})
    
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login')
    #     return render(request, self.template_name, {'form':form})




def my_profile(request):
    if request.method == 'GET':
        driver_profile = get_object_or_404(Driver, user=request.user)
        return render(request, 'my_profile.html', {'driver_profile': driver_profile})
    else:
        return HttpResponseNotAllowed(['GET']) 