from django.urls import path
from . import views 

urlpatterns = [
    path('', views.getRoutes),
    path('restaurants/', views.getRestaurants),
    path('restaurants/<str:pk>/', views.getRestaurant),
    path('offers/', views.getOffers),
    path('offers/<str:pk>/', views.getOffer),
    path('events/', views.getEvents),
    path('events/<str:pk>/', views.getEvent),
]