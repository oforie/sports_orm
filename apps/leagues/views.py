from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.filter(first_name = 'Alexander')|Player.objects.filter(first_name = 'Wyatt')
	}
# players
	# player with last_name 'Cooper' =  Player.objects.filter(last_name = 'Cooper')
	# first_name is 'Joshua' = Player.objects.filter(first_name = 'Joshua')
	# Players with last_name 'Cooper' but not 'Joshua' as first_name = Player.objects.filter(last_name = 'Cooper').exclude(first_name='Joshua')
	# players with first_name 'Alexander' or 'Wyatt' = Player.objects.filter(first_name = 'Alexander')|Player.objects.filter(first_name = 'Wyatt')
	


# Teams
	# teams in Dallas = Team.objects.filter(location__contains='dallas')
	# teams name the Raptors = Team.objects.filter(team_name__contains='raptor')
	# team location contains city = Team.objects.filter(location__contains='city'),
	# team name starts with "T" = Team.objects.filter(team_name__startswith='T')
	# Can't quite figure out how to order teams by alphebetical order

# leagues
	# all baseball leagues = League.objects.filter(name='baseball')
	# all womens' league = league.object.filter(name='baseball')
	# all league where sports is hockey = league.object.filter(name='baseball')
	# leagues other than football = league.objects.exclude(name__contains="Football")
	# contains conference = League.objects.filter(name__contains='Conference')
	# atlantic region = League.objects.filter(name__contains='atlantic')

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")