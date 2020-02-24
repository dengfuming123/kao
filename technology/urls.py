from django.urls import re_path
import technology.views
from django.urls import path, include
urlpatterns = [
 path('<int:n>/', technology.views.pagetegy),

]