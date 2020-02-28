from django.urls import re_path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('login.html', views.loginView, name='login'),
 path('register.html', views.registerView, name='register'),
 # path('setpassword.html', views.setpasswordView, name='setpassword'),
 path('logout.html', views.logoutView, name='logout'),
 path('FindPassword.html', views.findPassword, name='findPassword'),
 path('member/<int:n>', views.memberView),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)