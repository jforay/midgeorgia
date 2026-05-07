from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipment/', views.equipment, name='equipment'),
    path('first-responders/', views.first_responders, name='first_responders'),
    path('dirty-work/', views.dirty_work, name='dirty_work'),
    path('get-back/', views.get_back, name='get_back'),
]