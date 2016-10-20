from bet.models import  Match

def get_not_finished_matches():


    #ciekawe czy by renderowalo generator???
    ongoing_matches = []

    for match in list(Match.objects.all()):
        if (not match.home_goals) and (not match.away_goals):
           ongoing_matches.append(match)

    return ongoing_matches

