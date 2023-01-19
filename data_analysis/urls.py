from django.urls import path
from . import views

urlpatterns = [
    path('analytics',views.analytics, name='analytics'),
    path('generate_pdf',views.generate_pdf, name='generate_pdf')
]