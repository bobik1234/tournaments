import operator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from bet.models import Bet, Match
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from bet.forms import Vote
from bet.summary import get_finished_votes
from bet.utility import calculate_current_bets

def index(request):
    return HttpResponse("Hello, world. Mamy strone z zakladami")

@login_required(login_url='/accounts/login/')
def summary_table(request):

    overview_results = get_finished_votes()
    summary = calculate_current_bets(overview_results)

    context = {'overview_results' : overview_results,
               'summary' : summary}
    return render(request, 'bet/summary_table.html', context)

@login_required(login_url='/accounts/login/')
def own_calculation(request):
    context = {}
    return render(request, 'bet/own_calculation.html', context)

@login_required(login_url='/accounts/login/')
def my_results(request):

    overview_results = get_finished_votes(user=request.user)
    summary = calculate_current_bets(overview_results)

    context = {'overview_results': overview_results,
               'summary' : summary}
    return render(request, 'bet/my_results.html', context)


@login_required(login_url='/accounts/login/')
def vote(request):
    user_bets = []
    for bet in list(Bet.objects.filter(user=request.user)):
        user_bets.append(bet)

    matches_to_bet = []
    id_matches_to_bet = []
    matches_already_bet = [m.match for m in user_bets]
    for match in list(Match.objects.all()):
        if match not in matches_already_bet:
            matches_to_bet.append(match)
            id_matches_to_bet.append(match.id)

    context = {'user_bets' : user_bets,
               'matches_to_bet' : matches_to_bet}

    request.session['id_matches_to_bet'] = id_matches_to_bet

    return render(request, 'bet/vote.html', context)


@login_required(login_url='/accounts/login/')
def new_votes(request):

    matches_to_bet = []
    for id in request.session['id_matches_to_bet']:
        matches_to_bet.append(Match.objects.get(pk=id))

    form = Vote(request.POST or None, matches_to_bet=matches_to_bet)
    if form.is_valid():
        own_results = {}
        for (team_name, score) in form.predicted_result():
            own_results[team_name] = score
            print (team_name)
            print (score)

        for match in matches_to_bet:
            print(match.home_team.name)
            m = Bet(user=request.user,
                    match = match,
                    expected_home_goals = own_results[match.home_team.name],
                    expected_away_goals = own_results[match.away_team.name])
            m.save()

        return render(request, 'bet/vote.html')
    context = {'matches_to_bet' : matches_to_bet,
               'form': form}
    return render(request, 'bet/new_votes.html', context,  RequestContext(request))

