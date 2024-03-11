from django.urls import path
from .import views


urlpatterns = [
    path('Register/',views.Register, name='Register'),
    path('Login/', views.Login,name='Login'),
    path('profileCreation/', views.profileCreation, name='createProfile'),
    path('', views.Home, name='Homepage'),
    path('Profile/',views.Profile,name='Profile'),
    path('Chat/',views.Chat,name='Chat'),
]
