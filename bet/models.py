from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

class Match(models.Model):
    home_team = CountryField()
    away_team = CountryField()
    ROUND = (('1','one'), ('2','two'), ('3','three'), ('4','four'), ('5',"five"), ('6', 'six'))
    round = models.CharField(
        max_length=2,
        choices=ROUND,
        default='1',
    )
    home_goals = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    away_goals = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    match_date = models.DateTimeField('match date', blank=True, null=True)

    def __str__(self):
        return '{} - {} {} Reslut: {} : {}'.format(self.home_team.name,
                                                   self.away_team.name,
                                                   self.match_date,
                                                   self.home_goals,
                                                   self.away_goals,)

class Bet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    expected_home_goals = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    expected_away_goals = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return 'User: {} Match: {} - {} Bet: {} : {}'.format(self.user,
                                                             self.match.home_team.name,
                                                             self.match.away_team.name,
                                                             self.expected_home_goals,
                                                             self.expected_away_goals)
