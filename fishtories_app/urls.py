from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('sign_up', views.sign_up),
    path('log_in', views.log_in),
    path('sign_out', views.sign_out),
    path('username_validate', views.username_validate),
    path('whoami', views.who_am_i),
    path('catch', views.catch),
    path('new_catch', views.new_catch),
    path('update_catch', views.update_catch),
    path('fishdb', views.fish_db),
    path('fishdbbyid', views.fishdb_byid),
    path('edit_user', views.edit_user),
    path('fish_data', views.get_fish_data),
    path('API/<str:zipcode>', views.weather_api),
    path('forecast/<str:zipcode>', views.forecast_api),
    re_path(r'^', views.home_page),
]
