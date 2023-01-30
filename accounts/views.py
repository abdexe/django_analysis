from django.shortcuts import render,redirect
from django.contrib import messages,auth
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from companiees.models import Companie

# Create your views here.


def login(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = auth.authenticate(username=username, password=password)

      if user is not None:
        auth.login(request, user)
        messages.success(request, 'You are now logged Out')
        return redirect('profile')
      else:
        messages.error(request,'Invalid credentials')
        return redirect('login')
    else:
      return render(request,'accounts/login.html')
    
def register(request):
    if request.method == 'POST':
      #Get form values
      username = request.POST['username']
      email = request.POST['email']
      gender = request.POST['gender']
      city = request.POST['city']
      age = request.POST['age']
      password = request.POST['password']
      cpassword = request.POST['cpassword']
      #check if passwords match
      if password == cpassword:
        #check username
        if CustomUser.objects.filter(username=username).exists():
          messages.error(request,'That username is taken')
          return redirect('register')
        else:
          if CustomUser.objects.filter(email=email).exists():
             messages.error(request,'That email is being used')
             return redirect('register')
          else:
            # Looks good
            
            id = CustomUser.objects.count() + 1
            user = CustomUser.objects.create_user(id=id,username=username,email=email,
            age=age,password=password,city=city,gender=gender)
            user.save()
            messages.success(request,'You are now registered and can login')
            return redirect('login')

      else:
        messages.error(request,'Passwords do not match')
        return redirect('register')
    else:
      return render(request,'accounts/register.html')

@login_required(login_url='/accounts/login')
def dashbord(request):
    return render(request,'accounts/dashbord.html')

@login_required(login_url='/accounts/login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
@login_required(login_url='/accounts/login')
def companie(request):
  companies = Companie.objects.all()

  context = {
    'companies': companies
  }
  return render(request,'accounts/companie.html',context)

@login_required(login_url='/accounts/login')
def profile(request):
  users = CustomUser.objects.all()
  
  context = {
    'users': users
  }
  return render(request,'accounts/profile.html',context)

def update_profile(request):
  if request.method == 'POST':
      CustomUser.objects.filter(username=request.POST['username']).update(
      age=request.POST['age'],city=request.POST['city']
      ,country=request.POST['country'],
      email=request.POST['email'])
      return render(request,'accounts/profile.html')


