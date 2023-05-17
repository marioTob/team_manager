from django.urls import path
from . import views


urlpatterns = [
    path('user/', views.users, name='users'),
    path('user/add/', views.addUser, name='add-user'),
    path('user/<str:id>/', views.user, name='user'),
    path('user/<str:id>/delete/', views.deleteUser, name='delete-user'),
    path('user/<str:id>/update/', views.updateUser, name='update-user'),

    path('place/', views.places, name='places'),
    path('place/add/', views.addPlace, name='add-place'),
    path('place/<str:id>/', views.place, name='place'),
    path('place/<str:id>/delete/', views.deletePlace, name='delete-place'),
    path('place/<str:id>/update/', views.updatePlace, name='update-place'),
]
