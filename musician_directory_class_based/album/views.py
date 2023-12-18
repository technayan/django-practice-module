from django.shortcuts import render
from album.forms import albumForm
from album.models import Album
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AddAlbum (CreateView):
    model = Album
    form_class = albumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('add_album')

class EditAlbum (UpdateView):
    model = Album
    form_class = albumForm
    pk_url_kwarg = 'id'
    template_name = 'album/edit_album.html'
    success_url = reverse_lazy('home')
