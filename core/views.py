from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from librarian.models import Student, Book

@login_required(login_url='/login/')
def hello(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("<center>You are not authorized to view this!</center>")
    else:
        if profile.user_type=='ADM':
            libs = Profile.objects.filter(
                user_type='LIB'
            )
            return render(request, 'admin_home.html', {"libs": libs}, status=200)
        elif profile.user_type=='LIB':
            students = Student.objects.all()
            books = Book.objects.all()
            return render(request, 'librarian_home.html', 
            {"students": students, "books": books}, status=200)
        else:
            return HttpResponse(
                "<center>\
                    You do not have the required permissions to view this.\
                    If you are a librarian, contact the Library administrator.\
                <br><br>\
                <a href='/login'>Logout</a>\
                </center>"
            )

def signup(request):
   if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                user_type='GST'
            )
            login(request, user)
            return redirect('hello')
   else:
       form = SignupForm()
   return render(request,'signup.html',{'form':form})
   
def log_in(request):
    if request.method == 'POST':
        user=authenticate(request,username=request.POST['username'],
        password=request.POST['password'])
        if user is not None:
            print(user)
            login(request,user)
            return redirect('hello')
        else:
            form = AuthenticationForm(request.POST)
            return render(request,'login.html',{'form':form, 'message':'Invalid Credentials'}, status=400)
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def show_guests(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='ADM':
            gst_profiles = Profile.objects.filter(user_type='GST')
            return render(request,'show_guests.html',{'guests':gst_profiles})
        else:
            return HttpResponseForbidden("You are not authorized to view this.")
        
@login_required(login_url='/login/')
def add_librarian(request, profile_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        print(profile)
        if profile.user_type=='ADM':
            try:
                profile = Profile.objects.get(pk=profile_id)
            except:
                raise Http404("Profile not found!")
            else:
                if profile.user_type=='GST':
                    profile.user_type='LIB'
                    profile.save()
                    return redirect('hello')
                elif profile.user_type=='ADM':
                    return HttpResponseForbidden('The profile corresonds \
                        to an administrator and cannot be changed.')
                else:
                    return HttpResponseForbidden("The profile is already a librarian!")
        else:
            return HttpResponseForbidden("You are not authorized to view this.")
    
@login_required(login_url='/login/')
def delete_librarian(request, profile_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponse("You are not authorized to view this.")
    else:
        if profile.user_type=='ADM':
            try:
                profile = Profile.objects.get(pk=profile_id)
            except:
                return Http404("Profile Not Found!")
            else:
                if profile.user_type=='LIB':
                    profile.user_type='GST'
                    profile.save()
                    return redirect('hello')
                else:
                    raise Http404("The requested profile doesn't correspond to a librarian!")
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url='/login/')
def register_lib(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponse("No such Administrator exists!")
    else:
        if profile.user_type=='ADM':
            if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    Profile.objects.create(
                        user=user,
                        user_type='LIB'
                    )
                    return redirect('hello')
            else:
                form = SignupForm()
            return render(request,'register_lib.html',{'form':form})
        else:
            return HttpResponseForbidden("You are not authorized to view this.")
