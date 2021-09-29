from django.shortcuts import render, get_object_or_404
from .models import Player, Matches, Image, Managers



def homepage(request):
    images=Image.objects.all()
    return render(request,'club/home.html',{'images':images})

def players(request):
    players=Player.objects.all()
    return render(request,'club/players.html',{'players':players})


def matches(request):
    matches=Matches.objects.filter().order_by('date')
    return render(request,'club/matches.html',{'matches':matches})

def management(request):
    managers=Managers.objects.all()
    return render(request,'club/management.html',{'managers':managers})

def showplayer(request,player_id):
    player=get_object_or_404(Player,pk=player_id)
    return render(request,'club/showplayer.html',{'player':player})