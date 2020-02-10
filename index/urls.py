from django.urls import re_path
from index.views import index, showpost, writepost, recordpost
from django.urls import path, include
urlpatterns = [
 path('', index),
 path('post/<id>/', showpost),
 path('submit.html', writepost),
 path('record/<user_id>/', recordpost),
]