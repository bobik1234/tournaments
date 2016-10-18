from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^summary_table/$', views.summary_table, name='summary_table'),
    url(r'^my_results/$', views.my_results, name='my_results'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^new_votes/$', views.new_votes, name='new_votes'),
    url(r'^own_calculation/$', views.own_calculation, name='own_calculation'),
]
