from typing import Any
from django.shortcuts import render
from musician.forms import musicianForm
from musician.models import Musician
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = musicianForm
    success_url = reverse_lazy('add_musician')
    template_name = 'musician/add_musician.html'


class EditMusician (UpdateView):
    model = Musician
    form_class = musicianForm
    template_name = 'musician/edit_musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


@method_decorator(login_required, name='dispatch')
class DeleteMusician (DeleteView):
    model = Musician
    pk_url_kwarg = 'id'
    template_name = 'musician/delete_musician.html'
    success_url = reverse_lazy('home')

    
    