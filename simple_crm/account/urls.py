from django.conf.urls import include, url
from account.views import registration, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^registration/$', registration, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'account/logout.html'}, name='logout'),
]
