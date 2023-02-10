from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.create_user),
    path('login/',views.login),
    path('update/<int:pk>/',views.update_user),
    path('delete/<int:pk>/',views.delete_user)
   
]