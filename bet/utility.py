import operator

def calculate_current_bets(overview_results):
    """

    :param overview_results:  - lista slownikow {'user' : bet.user,
                                                'match' : match,
                                                'expected_result' : _result_to_string(bet.expected_home_goals, bet.expected_away_goals),
                                                'final_result' : _result_to_string(match.home_goals, match.away_goals),
                                                'score' : score
    :return:
            result - slownik {'round' : {user : score,
                                         user : score)}...
                              'summary' : {user : score},
                                            {user : score}}
    """

    rounds_results = {'summary' : {}}

    for result in overview_results:
        round = result['match'].round
        if not (round in rounds_results.keys()):
            rounds_results[round] = {}

        if result['user'] in rounds_results[round].keys():
            rounds_results[round][result['user']] += result['score']
        else:
            rounds_results[round][result['user']] = result['score']

        if result['user'] in rounds_results['summary'].keys():
            rounds_results['summary'][result['user']] += result['score']
        else:
            rounds_results['summary'][result['user']] = result['score']

    #sortujemy slowniki

    sorted_rounds_results = {}
    for round, results in rounds_results.items():
       sorted_rounds_results[round] = sorted(results.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_rounds_results
