from Pye.views import Pyebar
from django.urls import path, include
urlpatterns = [
 path('', Pyebar, name='bar'),
]