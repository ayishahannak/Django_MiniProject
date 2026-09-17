from django.urls import path

from newApp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("food_form",views.food_data,name="menu_form"),
    path("menu_view",views.menu_view,name="menu_view"),
]