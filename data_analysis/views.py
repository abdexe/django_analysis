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
        
        
        see_brand_in = df['see_brand'].str.split(',',expand=True)
        see_brand_in.head()
        # print(see_brand_in.stack().value_counts(normalize=True))
        

        #rating analysis Yes answer feedback
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
        
        
        context1 = {
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
        
        # DATA ANALYSIS IN THE "NO" CASE
         #Things customers are looking for in a brand
        pq = df2['looking'].str.contains('A').value_counts().values[1]
        product_quality = (pq /df2.shape[0]) * 100 

        gp = df2['looking'].str.contains('B').value_counts().values[1]
        good_price = (gp / df2.shape[0]) * 100

        qp = df2['looking'].str.contains('C').value_counts().values[1]
        quality_and_price = (qp / df2.shape[0]) * 100

        ot = df2['looking'].str.contains('D').value_counts().values[1]
        other_things = (ot / df2.shape[0]) * 100
         #Difficulties faced by customers with the brand 
        high_price = df2['problems'].str.contains('A').value_counts().values[1]
        not_enough = df2['problems'].str.contains('B').value_counts().values[1]
        not_quality = df2['problems'].str.contains('C').value_counts().values[1]
        rare_product = df2['problems'].str.contains('D').value_counts().values[1]
         #Percentages of products that visitors are interested in
        p_clothings = df2['products'].str.contains('A').value_counts().values[1]
        p_shoes = df2['products'].str.contains('B').value_counts().values[1]
        p_access = df2['products'].str.contains('C').value_counts().values[1]
         #There may be people talking about our brand
        

         #Percentage of people curious about the brand
        s_brand = df2['speaking_brand'].str.contains('B').value_counts().values[1]
        speaking_brand = round((s_brand / df2.shape[0]) * 100,2)
        #The possibility of sharing the brand with other people
        one = df2['sharing_probabilite'].value_counts()[10]
        two = df2['sharing_probabilite'].value_counts()[20]
        three = df2['sharing_probabilite'].value_counts()[30]
        four = df2['sharing_probabilite'].value_counts()[40]
        five = df2['sharing_probabilite'].value_counts()[50]
        six = df2['sharing_probabilite'].value_counts()[60]
        seven = df2['sharing_probabilite'].value_counts()[70]
        eight = df2['sharing_probabilite'].value_counts()[80]
        nine = df2['sharing_probabilite'].value_counts()[90]
        teen = df2['sharing_probabilite'].value_counts()[100]
        
        

         #The extent to which visitors are satisfied with the brand's products and services
        ns1 = df2['rating_feedback'].value_counts()[1]
        n_star1 = (ns1 / df2.shape[0]) * 100
        ns2 = df2['rating_feedback'].value_counts()[2]
        n_star2 = (ns2 / df2.shape[0]) * 100
        ns3 = df2['rating_feedback'].value_counts()[3]
        n_star3 = (ns3 / df2.shape[0]) * 100
        ns4 = df2['rating_feedback'].value_counts()[4]
        n_star4 = (ns4 / df2.shape[0]) * 100
        ns5 = df2['rating_feedback'].value_counts()[5]
        n_star5 = (ns5 / df2.shape[0]) * 100

        context2 = {
            "product_quality" : product_quality,
            "good_price":good_price,
            "quality_and_price":quality_and_price,
            "other_things":other_things,

            "high_price":high_price,
            "not_enough":not_enough,
            "not_quality":not_quality,
            "rare_product":rare_product,

            "p_clothings":p_clothings,
            "p_shoes":p_shoes,
            "p_access":p_access,

            "speaking_brand":speaking_brand,

            "n_star1":n_star1,
            "n_star2":n_star2,
            "n_star3":n_star3,
            "n_star4":n_star4,
            "n_star4":n_star4,

            "one":one,
            "two":two,
            "three":three,
            "four":four,
            "five":five,
            "six":six,
            "seven":seven,
            "eight":eight,
            "nine":nine,
            "teen":teen

 
        }
        context = {**context1, **context2}
    return render(request,'accounts/analytics.html',context)


        
        
        
        
   
     

    
     
    



