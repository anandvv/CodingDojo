from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker


def index(request):
	context = {
		"baseball_leagues": League.objects.filter(sport__icontains='baseball'),
		"women_leagues": League.objects.filter(name__icontains='women'),
		"hockey_leagues": League.objects.filter(sport__icontains='hockey'),
		"notFootball_leagues": League.objects.exclude(sport__icontains='football'),
		"conferences": League.objects.filter(name__icontains='conference'),
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"cooper_players": Player.objects.filter(last_name__icontains='cooper'),
		"joshua_players": Player.objects.filter(first_name__icontains='joshua'),
		"coopersNotNamedJoshua": Player.objects.filter(last_name__icontains='cooper').exclude(first_name='Joshua'),
		"dallas_teams": Team.objects.filter(location__icontains='dallas'),
		"raptor_teams": Team.objects.filter(team_name__icontains='raptor'),
		"city_teams": Team.objects.filter(location__icontains='city'),
		"T_teams": Team.objects.filter(location__startswith='T'),
		"all_teams_ordered": Team.objects.all().order_by('location'),
		"all_teams_reverse_ordered_by_name": Team.objects.all().order_by('-team_name'),
		'alexanderOrWyatt': Player.objects.filter(first_name='Alexander') | Player.objects.filter(first_name='Wyatt')
	}
	return render(request, "leagues/index.html", context)


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")