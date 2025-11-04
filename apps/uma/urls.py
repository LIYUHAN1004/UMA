from django.urls import path
from . import views

app_name = 'uma'

urlpatterns = [
    path('', views.horse_filter_view, name='horse_filter'),
]
