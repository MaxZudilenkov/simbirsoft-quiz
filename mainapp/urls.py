from django.shortcuts import render
from django.urls import path

from mainapp.views import show_first_page, create_quiz

urlpatterns = [

    path('', show_first_page, name="show_first_page"),
    path('create_quiz/', create_quiz, name="create_quiz"),


]