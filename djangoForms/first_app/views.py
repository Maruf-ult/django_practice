from django.shortcuts import render
# from . forms import contactForm
from . forms import StudentData
from . forms import contactForm
from . forms import Authentication


def home(request):
    return render(request, "first_app/home.html")  # Ensure this template exists

def about(request):
     if request.method == 'POST' :
         print(request.POST)
         name = request.POST.get('username')
         email = request.POST.get('email')
         select = request.POST.get('select')
         return render(request, 'first_app/about.html',{'name': name,'email': email, 'select': select})
     else:
          return render(request, 'first_app/about.html') # Ensure `about.html` exists

def submit_form(request):

         return render(request, './first_app/form.html')

def DjangoForm(request):
 if request.method == 'POST':
     form = contactForm(request.POST, request.FILES)
     if form.is_valid():
        # file = form.cleaned_data['file']
        # with open('./first_app/upload/' + file.name, 'wb+' ) as destination:
        #      for chunk in file.chunks():
        #           destination.write(chunk)
        print(form.cleaned_data)
    #  return render(request,'./first_app/django_form.html',{'form':form})
     
 else:
        form = contactForm()
        return render(request, './first_app/django_form.html',{'form':form})
 
def StudentForm(request):
    form = StudentData()  # Ensure form is always available
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, './first_app/django_form.html', {'form': form})

def AuthForm(request):
    form = Authentication()
    if request.method == 'POST':
        print(request.POST)
        form = Authentication(request.POST)
        if form.is_valid():
              print(form.cleaned_data)
    return render(request, './first_app/django_form.html', {'form': form})
          