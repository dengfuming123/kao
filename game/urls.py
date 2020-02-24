from django.urls import re_path
import game.views
from django.urls import path, include
urlpatterns = [
 path('<int:n>/', game.views.pagetegy),

]