from django.urls import re_path
from index.views import index, showpost, writepost, recordpost, pagechange
from django.urls import path, include
urlpatterns = [
 path('', index, name='index'),
 re_path(r'^page/(?P<n>[a-zA-Z0-9]{1})/$', pagechange),
 path('post/<id>/', showpost),
 path('submit.html', writepost),
 path('record/<user_id>/', recordpost),
 path('accounts/', include('allauth.urls')),
 path('technology/', include('technology.urls')),
 path('game/', include('game.urls')),
 path('movie/', include('movie.urls')),
 path('qt/', include('QT.urls')),
]