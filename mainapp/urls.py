from django.shortcuts import render
from django.urls import path

from mainapp.views import show_first_page

urlpatterns = [

    path('', show_first_page, name="show_first_page"),


]