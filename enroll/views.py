from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showFormdata(request):
    if(request.method == 'POST'):
        fm = StudentRegistration(request.POST)
        if fm.is_valid(): 
            print("Form Validated !!! ")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['rpassword']

            print("Name : ", name)
            print("Email : ", email)
            print('password : ', password)
            print('rpassword : ', rpassword)

            return render(request, 'enroll/success.html', {'nm' : name})

    else:
        fm = StudentRegistration()
        print("ye Get Request he")

    return render(request, 'enroll/userRegistration.html', {'form' : fm})
