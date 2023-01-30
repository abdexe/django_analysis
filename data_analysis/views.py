from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.models import CustomUser
from surveys.models import Survey, Surveyno
import pdfkit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
from django.db import connection
from django.contrib.auth.decorators import login_required

#Data Analysis with Numpy & Pandas
@login_required(login_url='/accounts/login')
def analytics(request):
    # transfer answers "YES" to Pandas datafrmae
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM surveys_survey")
        df = pd.read_sql_query("SELECT * FROM surveys_survey", connection)
    
    # transfer answers "NO" to Pandas datafrmae
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM surveys_surveyno")
        df2 = pd.read_sql_query("SELECT * FROM surveys_surveyno", connection)

        # gender analysis
        male_no_numbers=df2['user_gender'].str.contains('Male').value_counts().values[0]
        male_yes_numbers=df['user_gender'].str.contains('Male').value_counts().values[0]
        male_numbers = male_yes_numbers + male_no_numbers
        
        female_no_numbers=df2['user_gender'].str.contains('Male').value_counts().values[1]
        female_yes_numbers=df['user_gender'].str.contains('Male').value_counts().values[1]
        female_numbers = female_no_numbers + female_yes_numbers

        never_heard_about_brand = male_no_numbers + female_no_numbers
        heard_about_brand = male_yes_numbers + female_yes_numbers
        # hearing about brand
        last_month=df['hear_brand'].str.contains('A').value_counts().values[1]
        six_month_ago=df['hear_brand'].str.contains('B').value_counts().values[1]
        last_year=df['hear_brand'].str.contains('C').value_counts().values[1]
        from_start =df['hear_brand'].str.contains('D').value_counts().values[1]
        
        
        # the percentage of people who see the brand by categorie
        from_family = df['see_brand'].str.contains('A').value_counts().values[1]
        from_socialmedia = df['see_brand'].str.contains('B').value_counts().values[1]
        from_tbleshow = df['see_brand'].str.contains('C').value_counts().values[1]
        from_tvshow = df['see_brand'].str.contains('D').value_counts().values[1]
        from_application = df['see_brand'].str.contains('E').value_counts().values[1]
        from_other = df['see_brand'].str.contains('F').value_counts().values[0]
        
        data = [from_family,from_socialmedia,from_tbleshow,from_tvshow,from_application,from_other]
        print(data)
        
        see_brand_in = df['see_brand'].str.split(',',expand=True)
        see_brand_in.head()
        # print(see_brand_in.stack().value_counts(normalize=True))
        

        #rating analysis
        star1 = df['rating_feedback'].value_counts()[1]
        star2 = df['rating_feedback'].value_counts()[2]
        star3 = df['rating_feedback'].value_counts()[3]
        star4 = df['rating_feedback'].value_counts()[4]
        star5 = df['rating_feedback'].value_counts()[5]
       
        MinyA= from_application = df['user_city'].str.contains('MinyA').value_counts().values[1]
        cairo = df['user_city'].value_counts()['cairo']
        Ismailia = df['user_city'].value_counts()['Ismailia']
        Alexandria = df['user_city'].value_counts()['Alexandria']
        Giza = df['user_city'].value_counts()['Giza']
        Dandarah = df['user_city'].value_counts()['Dandarah']

        surveys = Survey.objects.all()
        # DATA ANALYSIDS IN THE "NO" CASE
        
        context = {
            "male": male_numbers,
            "female":female_numbers,
            "heard":heard_about_brand,
            "never_heard":never_heard_about_brand,
            "last_month":last_month,
            "six_month_ago":six_month_ago,
            "last_year":last_year,
            "from_start":from_start,

            "from_family":from_family,
            "from_socialmedia":from_socialmedia,
            "from_tbleshow":from_tbleshow,
            "from_tvshow":from_tvshow,
            "from_application":from_application,
            "from_other":from_other,

            "answers":df.shape[0]+df2.shape[0],

            "star1":star1,
            "star2":star2,
            "star3":star3,
            "star4":star4,
            "star5":star5,
            
            "cairo":cairo,
            "MinyA":MinyA,
            "Dandarah":Dandarah,
            "Giza":Giza,
            "Alexandria":Alexandria
        }
        
    return render(request,'accounts/analytics.html',context)


        
        
        
        
   
     

    
     
    



