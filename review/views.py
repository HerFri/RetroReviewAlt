from django.shortcuts import render
from django.views import generic
from .models import Game, Review, Comment

# Create your views here.

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.all()   # .order_by('-rating')
    template_name = 'index.html'
    paginate_by = 6
