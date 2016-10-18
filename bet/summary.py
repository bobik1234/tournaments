from bet.models import Bet, Match


def get_finished_votes(user = None):
    """
    :return:
    """

    overview_results = []
    for match in list(Match.objects.all()):
        if (match.home_goals is None) or (match.away_goals is None):
            continue

        for bet in list(Bet.objects.all()):
            if match == bet.match:
                if user and (user == bet.user):
                    overview_results.append(_match_bet_calculation(bet, match))
                elif user is None:
                    overview_results.append(_match_bet_calculation(bet, match))
                else:
                    continue
    return overview_results

def _match_bet_calculation(bet, match):
    """
    """
    return {'user' : bet.user,
            'match' : match,
            'expected_result' : _result_to_string(bet.expected_home_goals, bet.expected_away_goals),
            'final_result' : _result_to_string(match.home_goals, match.away_goals),
            'score' :  _calculate_score(bet, match)}

def _calculate_score(bet, match):
    """
    """
    if (match.home_goals == bet.expected_home_goals) and (match.away_goals == bet.expected_away_goals):
        return 3
    elif _who_won(match.home_goals, match.away_goals) == _who_won(bet.expected_home_goals, bet.expected_away_goals):
        return 1
    else:
        return 0

def _who_won(home_goals, away_goals):
    """
    """
    if home_goals > away_goals:
        return "home team won"
    elif home_goals == away_goals:
        return "duce"
    else:
        return "away team won"

def _result_to_string(home_goals, away_goals):
    """
    """
    return "{hg}:{ag}".format(hg=home_goals, ag=away_goals)
