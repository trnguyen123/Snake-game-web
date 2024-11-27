from django.urls import path
from . import views
from .views import save_playing_history
from .views import get_playing_history


urlpatterns = [
    path('api/save-history/', save_playing_history, name='save_playing_history'),
    path('', views.index, name='index'),
    path('api/get-history/', get_playing_history, name='get_playing_history'),

]

