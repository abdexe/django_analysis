from django.contrib import admin
from .models import Survey, Surveyno

class SurveyAdmin(admin.ModelAdmin):
       
    list_display = ('user_id','user_age','user_country','user_gender','user_city','see_brand','use_before',
    'hear_brand','speaking_brand','buy_before','rating_experience','rating_feedback',
    'sharing_probabilite','other_brand','best_brand','comment')
    list_display_links = ('user_id','user_country','hear_brand','speaking_brand','use_before','see_brand','buy_before','other_brand','best_brand')
    list_per_page = 30
    

admin.site.register(Survey, SurveyAdmin)

class SurveynoAdmin(admin.ModelAdmin):
       
    list_display = ('user_id','user_age','user_country','user_gender','user_city','problems','products',
    'looking','speaking_brand','buy_before','rating_feedback',
    'sharing_probabilite','comment')
    list_display_links = ('user_id','user_country','user_city','speaking_brand','looking','products')
    list_per_page = 30
    

admin.site.register(Surveyno, SurveynoAdmin)