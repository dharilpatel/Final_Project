from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^Home/',views.Home, name='home'),
    url(r'^signup/',views.signup, name='signup'),
    url(r'^login/',views.auth_view, name='login')


]