from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from betting.models import Match, Bank, Owner
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MatchAvailableView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Match
    context_object_name = 'my_match_list'
    queryset = Match.objects.filter(Q(match_status=2) | Q(match_status=3)).order_by('match_time').reverse()[:10]
    template_name = 'betting/match_available.html'
    paginate_by = 2


class MatchFinishView(LoginRequiredMixin, generic.ListView):
    model = Match
    context_object_name = 'my_match_list'
    queryset = Match.objects.filter(Q(match_status=4) | Q(match_status=5)).order_by('match_time').reverse()[:10]
    template_name = 'betting/match_finish.html'
    paginate_by = 2


class Payment(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Owner
    context_object_name = 'owner_list'
    queryset = Owner.objects.filter()[:1]
    template_name = 'betting/payment.html'
    paginate_by = 2


class Help(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Owner
    context_object_name = 'owner_list'
    queryset = Owner.objects.filter()[:1]
    template_name = 'betting/help.html'
    paginate_by = 5