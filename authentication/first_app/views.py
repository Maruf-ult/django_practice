from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

def home(request):
   return render(request,'./home.html')




def signup(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
         messages.success(request,'Account created successfully')
         messages.warning(request,'warning')
         messages.info(request,'infor')
         form.save()
         print(form.cleaned_data)
         return redirect('login')
            # instance.save()  # Actually saving the instance
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})  # Always return a response
 else:
    return redirect('profile') 

def user_login(request):
 if not request.user.is_authenticated:

   if request.method == 'POST':
      form = AuthenticationForm(request=request, data = request.POST)
      if form.is_valid():
         name = form.cleaned_data['username']
         userpass = form.cleaned_data['password']
         user = authenticate(username = name, password = userpass)
         if user is not None:
            login(request,user)
            return redirect('profile')
   else:
      form = AuthenticationForm()
  
   return render(request,'./login.html',{'form':form})

 else:
   return redirect('profile') 
def profile(request):
  if  request.user.is_authenticated:
     if request.method == 'POST':
        form = ChangeUserData(request.POST,instance = request.user)
        if form.is_valid():
         messages.success(request,'Account updated successfully')
         # messages.warning(request,'warning')
         # messages.info(request,'infor')
         form.save()
         print(form.cleaned_data)
            # instance.save()  # Actually saving the instance
     else:
        form = ChangeUserData(instance=request.user)

     return render(request, './profile.html', {'form': form})  # Always return a response
  else:
     return redirect('signup') 
  
  
def user_logout(request):
   logout(request)
   return redirect('login')


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Save the new password
            update_session_auth_hash(request, user)  # Keep the session authenticated
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'passchange.html', {'form': form})
   

def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Save the new password
            update_session_auth_hash(request, user)  # Keep the session authenticated
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)

    return render(request, 'passchange.html', {'form': form})



