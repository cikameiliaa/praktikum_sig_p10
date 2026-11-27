from django.urls import path
from . import views, viewspeta

urlpatterns = [
     path('welcome/', views.welcome,
         name='welcome'),

     path('petasatu/', viewspeta.petasatu,
         name='petasatu'),

     path('petadua/', viewspeta.petadua,
         name='petadua'),

     path('petakampus/', viewspeta.petakampus,
           name='petakampus'),

     path('peta_provinsi/', viewspeta.peta_provinsi,
           name='peta_provinsi'),
           
     path('petani_jawa/', viewspeta.petani_jawa,
           name='petani_jawa'),
]