"""Proto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from betting import views as betting_view
from account.views import home_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admintools/', include('admin_tools.urls')),

    path('match/available/', betting_view.MatchAvailableView.as_view(), name='matchs_available'),
    path('match/finish/', betting_view.MatchFinishView.as_view(), name='matchs_finish'),
    path('payment/', betting_view.Payment.as_view(), name='payment'),
    path('help/', betting_view.Help.as_view(), name='help'),

    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),

    path('accounts/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
