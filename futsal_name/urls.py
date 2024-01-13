from django.urls import path 
from . import views 


urlpatterns = [
     path('', views.home, name="home"),
     path('<int:year>/<str:month>/', views.home, name="home"),
     path('futsalbooking_list/', views.all_futsalbooking_list, name="futsalbooking_list"),
     path('add_futsal/', views.add_futsal, name='add-futsal'),
     path('futsal_list/', views.all_futsals_list, name='futsals_list'),
     path('futsal_show/<futsal_id>/', views.futsals_show, name='futsals_show'),
     path('futsal_search/', views.futsals_search, name='futsals_search'),
     path('futsal_update/<futsal_id>/', views.futsals_update, name='futsals_update'),
     path('futsalbooking_add/', views.futsalbooking_add, name="futsalbooking_add"),
]
