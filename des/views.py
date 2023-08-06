from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def main_page(request):
    contex={'title':'Disney+ Home'}
    return render(request,'index.html',contex)


@login_required(login_url='/login/')
def movie(request):
    quertset=Marvel.objects.all()
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'Disney+ Movie'}
    return render (request,'movie.html',contex)


@login_required(login_url='/login/')
def view_movies(request,id):
    quertset =Marvel.objects.get(id=id)
    contex={'items':quertset,'title':'Disney+ View Movies'}
    return render (request,'view_movies.html',contex)


@login_required(login_url='/login/')
def marver_movies(request):
    quertset=Marvel.objects.filter(category__name="Marvel")
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'Disney+ Marver movies'}
    return render (request,'movie.html',contex)

@login_required(login_url='/login/')
def Pixar_movies(request):
    quertset=Marvel.objects.filter(category__name="Pixar")
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'Pixar Movies'}
    return render (request,'movie.html',contex)

@login_required(login_url='/login/')
def Disney_movies(request):
    quertset=Marvel.objects.filter(category__name="Disney")
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'Disney+ Movies'}
    return render (request,'movie.html',contex)
@login_required(login_url='/login/')
def N_G_movies(request):
    quertset=Marvel.objects.filter(category__name="National Geographic")
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'National Geographic'}
    return render (request,'movie.html',contex)

@login_required(login_url='/login/')
def Star_movies(request):
    quertset=Marvel.objects.filter(category__name="Star Wars")
    if request.GET.get('search'):
        quertset= quertset.filter(movie_name__icontains = request.GET.get('search'))

    # contex={'items':quertset}
    contex={'items':quertset,'title':'Star Movies'}
    return render (request,'movie.html',contex)


@login_required(login_url='/login/')
def my_profile(request):
    return render (request,'profile.html',{'title':'Profile'})

def signup(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User Name already taken')
            redirect('/signup/')
        user =User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created Successfully')

    return render(request,'signUp.html',{'title':'Signup'})

def login_page(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html',{'title':'Login'})

def logout_page(request):
    logout(request)
    messages.info(request,'Logout Successful')
    return redirect('/login/')