from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect
from games import forms
from games.models import Publisher, Platform, Game, Genre


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class GamesView(View):
    def get(self, request):
        platforms = Platform.objects.all()
        publishers = Publisher.objects.all()
        genres = Genre.objects.all()
        games = Game.objects.all()
        gameForm = forms.GameForm
        return render(request, 'general_view.html',
                      {'platforms': platforms, 'publishers': publishers, 'genres': genres, 'objects': games,
                       'form': gameForm})

    def post(self, request):
        form = forms.GameForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/games/')
        platforms = Platform.objects.all()
        publishers = Publisher.objects.all()
        genres = Genre.objects.all()
        games = Game.objects.all()
        return render(request, 'general_view.html.html',
                      {'platforms': platforms, 'publishers': publishers, 'genres': genres, 'objects': games,
                       'form': gameForm})


class GenreView(View):
    def get(self, request):
        genres = Genre.objects.all()
        genreForm = forms.GenreForm()
        return render(request, 'general_view.html', {'objects': genres, 'form': genreForm})

    def post(self, request):
        genreForm = forms.GenreForm(request.POST)
        if genreForm.is_valid():
            genreForm.save()
            return redirect('/genres')
        genres = Genre.objects.all()
        return render(request, 'general_view.html', {'objects': genres, 'form': genreForm})


class PublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        publisherForm = forms.PublisherForm()
        return render(request, 'general_view.html', {'objects': publishers, 'form': publisherForm})

    def post(self, request):
        publisherForm = forms.PublisherForm(request.POST)
        if publisherForm.is_valid():
            publisherForm.save()
            return redirect('/publishers')
        publishers = Publisher.objects.all()
        return render(request, 'general_view.html', {'objects': publishers, 'form': publisherForm})


class PlatformView(View):
    def get(self, request):
        platforms = Platform.objects.all()
        platformForm = forms.PlatformForm()
        return render(request, 'general_view.html', {'objects': platforms, 'form': platformForm})

    def post(self, request):
        platformForm = forms.PlatformForm(request.POST)
        if platformForm.is_valid():
            platformForm.save()
            return redirect('/platforms')
        platforms = Platform.objects.all()
        return render(request, 'general_view.html', {'objects': platforms, 'form': platformForm})
