from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.http import  HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class AdView(ListView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    
    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")
        ad=request.POST.get("pk")
        user=request.POST.get("user")
        Reply.objects.create(text=text,ad=Ad.objects.get(id=ad),user=User.objects.get(id=user))
        return HttpResponseRedirect("")

class NewAd(CreateView, LoginRequiredMixin):
    template_name = 'create.html'
    form_class = AdForm
    success_url = '/general/'


class UpdateAd(UpdateView):
    template_name = 'create.html'
    form_class = AdForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Ad.objects.get(pk=id)