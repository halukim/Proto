from django.contrib import admin

# Register your models here.
from .models import Match, Bank, Owner

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_time', 'match_status', 'final_odds', 'bet_amount', 'bet_devidends', 'team_name_1', 'team_name_2', 'team_name_3', 'team_name_4', 'team_odds_1', 'team_odds_2', 'team_odds_3', 'team_odds_4', 'match_condition_1', 'match_condition_2', 'match_desc_1', 'match_desc_2', 'match_result_1', 'match_result_2', 'betting_total', 'betting_now')
    list_filter = ('match_time', 'match_status')
    ordering = ['-match_time']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('code', 'bank_name', 'bank_account', 'email')
