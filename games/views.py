from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import F
from django.db.models.aggregates import Sum, Count
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect
from games import forms
from games.models import Publisher, Platform, Game, Genre
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


# games views

# widok listy gry
class GamesView(View):
    def get(self, request):
        games = Game.objects.all()
        return render(request, 'general_view.html', {'objects': games, 'link': 'games'})


# widok dodawania gry
class GamesAddView(View):
    def get(self, request):
        gameForm = forms.GameForm
        return render(request, 'form.html',
                      {'form': gameForm})

    def post(self, request):
        gameForm = forms.GameForm(request.POST)
        if gameForm.is_valid():
            gameForm.save()
            return redirect('/games/')
        return render(request, 'form.html', {'form': gameForm})


# Widok szczegółów gry
class GameDetail(View):
    def get(self, request, id):
        detail = Game.objects.get(pk=id)
        return render(request, 'game_details.html', {'detail': detail, 'id': id})

    def post(self, request, id):
        if '_edit' in request.POST:
            return redirect('/game/{}/update'.format(id))

        elif '_delete' in request.POST:
            game = Game.objects.get(pk=id)
            game.delete()
            return redirect('/games/')

        elif '_fav' in request.POST:
            game = Game.objects.get(pk=id)
            game.is_favorite.add(request.user)
            return redirect('/game/{}'.format(id))

        elif '_del' in request.POST:
            game = Game.objects.get(pk=id)
            game.is_favorite.remove(request.user)
            return redirect('/game/{}'.format(id))


class GameUpdateView(UpdateView):  # modyfikwanie elementu
    model = Game
    form_class = forms.GameForm
    template_name = 'form.html'
    success_url = '/games/'


# Genre views ---
# widok listy gatunków
class GenreView(View):
    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'general_view.html', {'objects': genres, 'link': 'genres'})


# widok dodawania gatunku
class GenreAddView(View):
    def get(self, request):
        genreForm = forms.GenreForm()
        return render(request, 'form.html', {'form': genreForm})

    def post(self, request):
        genreForm = forms.GenreForm(request.POST)
        if genreForm.is_valid():
            genreForm.save()
            return redirect('/genres')
        genres = Genre.objects.all()
        return render(request, 'form.html', {'form': genreForm})


# widok szczegółow gatunku
class GenreDetail(View):
    def get(self, request, id):
        detail = Genre.objects.get(pk=id)
        form = forms.GenreForm
        return render(request, 'details.html', {'detail': detail, 'form': form, 'id': id})

    def post(self, request, id):
        if '_edit' in request.POST:
            return redirect('/genre/{}/update'.format(id))

        elif '_delete' in request.POST:
            genre = Genre.objects.get(pk=id)
            genre.delete()
            return redirect('/genres/')


class GenreUpdateView(UpdateView):  # modyfikwanie elementu
    model = Genre
    form_class = forms.GenreForm
    template_name = 'form.html'
    success_url = '/genres/'


# Publisher views

# widok listy
class PublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'general_view.html', {'objects': publishers, 'link': 'publishers'})


# widok dodawania
class PublisherAddView(View):
    def get(self, request):
        publisherForm = forms.PublisherForm()
        return render(request, 'form.html', {'form': publisherForm})

    def post(self, request):
        publisherForm = forms.PublisherForm(request.POST)
        if publisherForm.is_valid():
            publisherForm.save()
            return redirect('/publishers')
        return render(request, 'form.html', {'form': publisherForm})


# widok szczegółów
class PublisherDetail(View):
    def get(self, request, id):
        detail = Publisher.objects.get(pk=id)
        return render(request, 'details.html', {'detail': detail, 'id': id})

    def post(self, request, id):
        if '_edit' in request.POST:
            return redirect('/publisher/{}/update'.format(id))

        elif '_delete' in request.POST:
            publisher = Publisher.objects.get(pk=id)
            publisher.delete()
            return redirect('/publishers/')


class PublisherUpdateView(UpdateView):  # modyfikwanie elementu
    model = Publisher
    form_class = forms.PublisherForm
    template_name = 'form.html'
    success_url = '/publishers/'


# Platform views

# widok listy
class PlatformView(View):
    def get(self, request):
        platforms = Platform.objects.all()
        return render(request, 'general_view.html', {'objects': platforms, 'link': 'platforms'})


# widok dodawania


class PlatformAddView(View):
    def get(self, request):
        platformForm = forms.PlatformForm()
        return render(request, 'form.html', {'form': platformForm})

    def post(self, request):
        platformForm = forms.PlatformForm(request.POST)
        if platformForm.is_valid():
            platformForm.save()
            return redirect('/platforms')
        return render(request, 'form.html', {'form': platformForm})


# widok szczegółowy
class PlatformDetail(View):
    def get(self, request, id):
        detail = Platform.objects.get(pk=id)
        return render(request, 'details.html', {'detail': detail, 'id': id})

    def post(self, request, id):
        if '_edit' in request.POST:
            return redirect('/platform/{}/update'.format(id))

        elif '_delete' in request.POST:
            platform = Platform.objects.get(pk=id)
            platform.delete()
            return redirect('/platforms/')


class PlatformUpdateView(UpdateView):  # modyfikwanie elementu
    model = Platform
    form_class = forms.PlatformForm
    template_name = 'form.html'
    success_url = '/platforms/'


# user profile

class UserProfile(LoginRequiredMixin, View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'user_profile.html', {'user': user})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        id_to_del = request.POST.get('_del')
        game = Game.objects.get(pk=id_to_del)
        game.is_favorite.remove(request.user)
        return redirect('/user/{}'.format(id))


# chart data

class GameChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id, format=None):
        game = Game.objects.get(pk=id)
        data = [game.na_sales, game.eu_sales, game.jp_sales]
        labels = ['na_sales', 'eu_sales', 'jp.sales']

        data = {
            'labels': labels,
            'data': data
        }

        return Response(data)


class GamesList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        games = Game.objects.values('name').order_by('name').annotate(
            total_sales=F('na_sales') + F('eu_sales') + F('jp_sales'))
        data = []
        labels = []

        for g in games:
            labels.append(g['name'])
            data.append(g['total_sales'])

        data = {
            'data': data,
            'labels': labels
        }
        return Response(data)


class GenresList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        games = Genre.objects.all().values('name').annotate(Count('game'))
        data = []
        labels = []

        for g in games:
            labels.append(g['name'])
            data.append(g['game__count'])

        data = {
            'data': data,
            'labels': labels
        }
        return Response(data)


class PublishersList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        publishers = Publisher.objects.all().values('name').annotate(Count('game'))
        data = []
        labels = []

        for g in publishers:
            labels.append(g['name'])
            data.append(g['game__count'])

        data = {
            'data': data,
            'labels': labels
        }
        return Response(data)


class PlatformsList(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        platforms = Platform.objects.all().values('name').annotate(Count('game'))
        data = []
        labels = []

        for g in platforms:
            labels.append(g['name'])
            data.append(g['game__count'])

        data = {
            'data': data,
            'labels': labels
        }
        return Response(data)
