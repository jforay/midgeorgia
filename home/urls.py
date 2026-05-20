from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipment/', views.equipment, name='equipment'),
    path('first-responders/', views.first_responders, name='first_responders'),
    path('dirty-work/', views.dirty_work, name='dirty_work'),
    path('get-back/', views.get_back, name='get_back'),
    path('amenities/', views.amenities, name='amenities'),
    path('weather/', views.weather, name='weather'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contact, name='contact'),
    path('banner/', views.banner, name='banner'),
]