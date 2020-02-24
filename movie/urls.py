from django.urls import re_path
import movie.views
from django.urls import path, include
urlpatterns = [
 path('<int:n>/', movie.views.pagetegy),

]