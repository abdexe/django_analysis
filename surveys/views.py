from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.models import CustomUser
from surveys.models import Survey,Surveyno
from django.contrib.auth.decorators import login_required

# FIRST SURVEY
@login_required(login_url='/accounts/login')
def survey(request):
    if request.method == 'POST':
      #Get form values
      hear_brand = request.POST['hear_time']
      speaking_brand = request.POST['speaking']
      buy_before = request.POST['buy_before']
      rating_experience = request.POST['rating1']
      rating_feedback = request.POST['rating2']
      sharing_probabilite = request.POST['rating']
      other_brand = request.POST['other']
      best_brand = request.POST['best_brand']

      options1 = request.POST.getlist('product[]')
      use_before= ','.join(map(str,options1))
      print(use_before)
      options2 = request.POST.getlist('see[]')
      see_brand = ','.join(map(str,options2))
      print(see_brand)
      comment = request.POST['comment']
      #addd
      user_id = request.POST['user_id']
      user_age = request.POST['user_age']
      user_country = request.POST['user_country']
      if comment == '':
        messages.error(request,'Please Fill the form')
      else:
        id = Survey.objects.count() + 1
        survey = Survey(id=id,user_id=user_id,user_age=user_age,user_country=user_country,
        hear_brand=hear_brand,speaking_brand=speaking_brand,buy_before=buy_before,
        rating_experience=rating_experience,rating_feedback=rating_feedback,use_before=use_before,
        see_brand=see_brand,sharing_probabilite=sharing_probabilite,other_brand=other_brand,
        best_brand=best_brand,comment=comment)
        survey.save()
        messages.success(request,'شكرا لقد تم ارسال معلوماتك بنجاح')
      return redirect('survey')
    else:
        return render(request,'accounts/survey.html')
      

# Second Survey

@login_required(login_url='/accounts/login')
def surveyno(request):
    if request.method == 'POST':
      #Get form values
      looking = request.POST['looking']
      speaking_brand = request.POST['speaking']
      buy_before = request.POST['buy_before']
      rating_feedback = request.POST['rating2']
      sharing_probabilite = request.POST['rating']

      options1 = request.POST.getlist('product[]')
      products = ','.join(map(str,options1))
      print(products)
      options2 = request.POST.getlist('see[]')
      problems = ','.join(map(str,options2))
      print(problems)
      comment = request.POST['comment']
      #addd
      user_id = request.POST['user_id']
      user_age = request.POST['user_age']
      user_country = request.POST['user_country']
      if comment == '':
        messages.error(request,'Please Fill the form')
      else:
        id = Surveyno.objects.count() + 1
        surveyno = Surveyno(id=id,user_id=user_id,user_age=user_age,user_country=user_country,
        looking=looking,speaking_brand=speaking_brand,buy_before=buy_before,
        rating_feedback=rating_feedback,products=products,
        problems=problems,sharing_probabilite=sharing_probabilite,
        comment=comment)
        surveyno.save()
        messages.success(request,'شكرا لقد تم ارسال معلوماتك بنجاح')
      return redirect('survey')
    else:
        return render(request,'accounts/survey.html')
      
        
        
        
        
   
     

    
     
    




        
        
        
   
     

    
     
    



