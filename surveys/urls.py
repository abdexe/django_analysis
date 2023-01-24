from django.urls import path
from . import views

urlpatterns = [
    path('survey',views.survey, name='survey'),
    path('surveyno',views.surveyno, name='surveyno')
]