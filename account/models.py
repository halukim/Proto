from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    nickname.verbose_name = "아이디"
    bank_name = models.CharField(max_length=20)
    bank_name.verbose_name = "은행 이름"
    bank_account = models.CharField(max_length=20)
    bank_account.verbose_name = "계좌번호"
    savings = models.PositiveIntegerField(default=0)
    savings.verbose_name = "적립"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()