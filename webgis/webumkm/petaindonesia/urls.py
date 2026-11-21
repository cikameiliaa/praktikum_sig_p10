from django.urls import path
from . import views, viewspeta

urlpatterns = [
    path('welcome/', views.welcome,
         name='welcome'),
    path('petasatu/', viewspeta.petasatu,
         name='petasatu'),
    path('petadua/', viewspeta.petadua,
         name='petadua'),
]