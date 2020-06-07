import math
from django.db import models

import uuid # Required for unique book instances

class Match(models.Model):

    match_time = models.DateTimeField(null=True, blank=True)
    match_time.verbose_name = "경기 시간"

    team_name_1 = models.CharField(max_length=100)
    team_name_2 = models.CharField(max_length=100)
    team_name_3 = models.CharField(max_length=100)
    team_name_4 = models.CharField(max_length=100)
    team_name_1.verbose_name = "1경기 첫번째 팀 이름(선택)"
    team_name_2.verbose_name = "1경기 두번째 팀 이름"
    team_name_3.verbose_name = "2경기 첫번째 팀 이름(선택)"
    team_name_4.verbose_name = "2경기 두번째 팀 이름"

    team_odds_1 = models.CharField(max_length=20)
    team_odds_2 = models.CharField(max_length=20)
    team_odds_3 = models.CharField(max_length=20)
    team_odds_4 = models.CharField(max_length=20)
    team_odds_1.verbose_name = "1경기 첫번째 팀 배당률"
    team_odds_2.verbose_name = "1경기 두번째 팀 배당률"
    team_odds_3.verbose_name = "2경기 첫번째 팀 배당률"
    team_odds_4.verbose_name = "2경기 두번째 팀 배당률"

    MATCH_CONDITION = (
        ('U', '언더'),
        ('O', '오바'),
    )

    match_condition_1 = models.CharField(
        max_length=1,
        choices=MATCH_CONDITION,
        blank=True,
        default='U',
        help_text='1경기 첫번째 팀 기준 언더-오바',)
    match_condition_2 = models.CharField(
        max_length=1,
        choices=MATCH_CONDITION,
        blank=True,
        default='U',
        help_text='2경기 첫번째 팀 기준 언더-오바', )
    match_condition_1.verbose_name = "1경기 첫번째 팀 기준 언더-오바"
    match_condition_2.verbose_name = "2경기 첫번째 팀 기준 언더-오바"

    match_desc_1 = models.CharField(default='0점', max_length=100)
    match_desc_2 = models.CharField(default='0점', max_length=100)
    match_desc_1.verbose_name = "1경기 첫번째 팀 기준 언오바 점수"
    match_desc_2.verbose_name = "2경기 첫번째 팀 기준 언오바 점수"

    MATCH_RESULT = (
        ('1', '경기 종료 전'),
        ('2', '적중'),
        ('3', '미적중'),
        ('4', '적특'),
    )

    match_result_1 = models.CharField(
        max_length=1,
        choices=MATCH_RESULT,
        blank=True,
        default='1',
        help_text='1경기 첫번째 팀 기준 결과', )
    match_result_2 = models.CharField(
        max_length=1,
        choices=MATCH_RESULT,
        blank=True,
        default='1',
        help_text='2경기 첫번째 팀 결과', )
    match_result_1.verbose_name = "1경기 결과"
    match_result_2.verbose_name = "2경기 결과"

    betting_total = models.CharField(default='10', max_length=20)
    betting_now = models.CharField(default='0', max_length=20)
    betting_total.verbose_name = "배팅 가능 수"
    betting_now.verbose_name = "배팅 참여 수"

    MATCH_STATUS = (
        ('1', '관리자 준비'),
        ('2', '베팅 진행'),
        ('3', '베팅 종료'),
        ('4', '경기 시작'),
        ('5', '경기 종료'),
    )

    match_status = models.CharField(
        max_length=1,
        choices=MATCH_STATUS,
        blank=True,
        default='1',
        help_text='해당 결기에 대한 관리 상태',
    )
    match_status.verbose_name = "경기 상태"

    class Meta:
        ordering = ['match_time', 'match_status']

    def __str__(self):
        return f'{self.match_time}'

    def final_odds(self):
        return round(float(self.team_odds_1) * float(self.team_odds_3), 2)

    def bet_ratio(self):
        return math.ceil(100 * float(self.betting_now) / float(self.betting_total))

    def bet_amount(self):
        return str(math.ceil(300 / (float(self.team_odds_1) * float(self.team_odds_3)))) + ' 만원'

    def bet_devidends(self):
        result = 300
        if (self.match_result_1 == "3") | (self.match_result_2 == "3"):
            result = 0
        elif self.match_result_1 == "4":
            result = math.ceil(result / float(self.team_odds_1))
        elif self.match_result_2 == "4":
            result = math.ceil(result / float(self.team_odds_3))
        return str(result) + ' 만원'


class Bank(models.Model):

    name = models.CharField(max_length=20)
    name.verbose_name = "은행"

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Owner(models.Model):

    code = models.CharField(default='1004', max_length=10)
    code.verbose_name = "가입 코드"
    bank_name = models.CharField(max_length=20)
    bank_name.verbose_name = "입금 은행 이름"
    bank_account = models.CharField(max_length=20)
    bank_account.verbose_name = "입금 계좌번호"
    email = models.CharField(max_length=40)
    email.verbose_name = "이메일"