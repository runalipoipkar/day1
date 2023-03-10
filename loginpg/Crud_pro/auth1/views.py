from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def sign_view(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage_url')
    template_name='auth1/signup.html'
    context={'form':form}
    return render(request, template_name, context)


def login_view(request):
    template_name='auth1/login.html'
    context={}
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        print(u,'=====',p)

        user=authenticate(username=u,password=p)

        if user is not None:
            login(request,user)
            return redirect('show_url')
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('loginPage_url')