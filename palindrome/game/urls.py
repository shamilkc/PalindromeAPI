from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.create_game),
    path('update/<int:pk>/', views.update_board),
    path('board/<int:pk>/', views.get_board),
    path('list/', views.list),
]