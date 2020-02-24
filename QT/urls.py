from django.urls import re_path
import QT.views
from django.urls import path, include
urlpatterns = [
 path('<int:n>/', QT.views.pagetegy),

]