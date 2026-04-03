from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.admin_page, name='admin_page'),
    path('league/', views.league_table, name='league'),
    path('team/<int:pk>/', views.team_detail, name='detail'),
    path('logout/', views.logout_page, name='logout')
]