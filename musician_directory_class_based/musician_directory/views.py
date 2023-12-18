from django.shortcuts import render
from album.models import Album
from django.views.generic import ListView


class AlbumView (ListView):
    model = Album
    template_name = 'index.html'
    success_url = 'home'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Album.objects.all()
        return context