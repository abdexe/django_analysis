from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('dashbord',views.dashbord, name='dashbord'),
    path('companie',views.companie, name='companie'),
    path('profile',views.profile, name='profile'),
    path('logout',views.logout, name='logout'),
    path('update_profile',views.update_profile, name='update_profile'),
    
]