from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib import auth



from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect


import json

from django.views import View
from django.http import JsonResponse

from .models import User


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('matchs_available')
        else:
            return render(request, 'account/login.html', {'error': '아이디 또는 비밀번호를 정확하게 입력해주세요.'})
    else:
        return render(request, 'account/login.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/sign_up.html'


def home_view(request):
    form = UserCreationForm(request.POST)
    return render(request, 'account/home.html', {'form': form})

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'account/signup.html', {'form': form})


class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            user_id=data['user_id'],
            password=data['password'],
        )

        if User.objects.filter(user_id = data['user_id']).exists() == True:
            return JsonResponse({"message": "이미 존재하는 아이디입니다."}, status=401)

        else:
            User.objects.create(user_id=data['user_id'], password=data['password'])
            return JsonResponse({"message": "회원으로 가입되셨습니다."}, status=200)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)


class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            user_id=data['user_id'],
            password=data['password']
        )

        if User.objects.filter(user_id=data['user_id'], password=data['password']).exists() == True :
            return JsonResponse({"message": "로그인에 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"message": "아이디나 비밀번호가 일치하지 않습니다."}, status=401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status=200)