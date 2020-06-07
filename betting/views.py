from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from betting.models import Match, Bank, Owner

# Create your views here.
class MatchAvailableView(generic.ListView):
    model = Match
    context_object_name = 'my_match_list'
    queryset = Match.objects.filter(Q(match_status=2) | Q(match_status=3)).order_by('match_time').reverse()[:3]
    template_name = 'betting/match_available.html'
    paginate_by = 2


class MatchFinishView(generic.ListView):
    model = Match
    context_object_name = 'my_match_list'
    queryset = Match.objects.filter(Q(match_status=4) | Q(match_status=5)).order_by('match_time').reverse()[:3]
    template_name = 'betting/match_finish.html'
    paginate_by = 2


class Payment(generic.ListView):
    model = Owner
    context_object_name = 'owner_list'
    queryset = Owner.objects.filter()[:1]
    template_name = 'betting/payment.html'
    paginate_by = 2


class Help(generic.ListView):
    model = Owner
    context_object_name = 'owner_list'
    queryset = Owner.objects.filter()[:1]
    template_name = 'betting/help.html'
    paginate_by = 5