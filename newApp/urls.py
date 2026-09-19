from django.urls import path

from newApp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("index",views.index,name="index"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("menu_form",views.food_data,name="menu_form"),
    path("menu_view",views.menu_view,name="menu_view"),
    path("menu_delete/<int:id>/",views.menu_delete,name="menu_delete"),
    path("menu_update/<int:id>/",views.menu_update,name="menu_update"),
]