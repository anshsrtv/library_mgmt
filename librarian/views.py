from django.shortcuts import render, redirect
from .models import Student, Book
from core.views import Profile
from .forms import StudentForm, BookForm, IssueForm
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/login/')
def add_student(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            if request.method == 'POST':
                form = StudentForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('hello')
                else:
                    return render(request, 'student.html', {"form":form}, status=400)
            else:
                form = StudentForm()
                return render(request, 'student.html', {"form":form}, status=200)
        else:   
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def add_book(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            if request.method == 'POST':
                form = BookForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('hello')
                else:
                    return render(request, 'book.html', {"form":form}, status=400)
            else:
                form = BookForm()
                return render(request, 'book.html', {"form":form}, status=200)
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def update_student(request, student_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                student = Student.objects.get(pk=student_id)
            except:
                raise Http404('Student Not Found!')
            else:
                if request.method == 'POST':
                    form = StudentForm(request.POST, instance=student)
                    if form.is_valid():
                        form.save()
                        return redirect('hello')
                    else:
                        return render(request, 'student.html', {"form":form}, status=400)
                else:
                    form = StudentForm(instance=student)
                    return render(request, 'student.html', {"form":form}, status=200)
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def update_book(request, book_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                book = Book.objects.get(pk=book_id)
            except:
                raise Http404('Book Not Found!')
            else:
                if request.method == 'POST':
                    form = BookForm(request.POST, instance=book)
                    if form.is_valid():
                        form.save()
                        return redirect('hello')
                    else:
                        return render(request, 'book.html', {"form":form}, status=400)
                else:
                    form = BookForm(instance=book)
                    return render(request, 'book.html', {"form":form}, status=200)
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def delete_student(request, student_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                student = Student.objects.get(pk=student_id)
            except:
                raise Http404('Student Not Found!')
            else:
                student.delete()
                return redirect('hello')
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def delete_book(request, book_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                book = Book.objects.get(pk=book_id)
            except:
                raise Http404('Book Not Found!')
            else:
                book.delete()
                return redirect('hello')
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def issue_book(request, book_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                book = Book.objects.get(pk=book_id)
            except:
                raise Http404('Book Not Found!')
            else:
                if request.method =='POST':
                    form = IssueForm(request.POST, instance=book)
                    book.issued = True
                    book.issue_date = datetime.date.today()
                    if form.is_valid():
                        form.save()
                        return redirect('hello')
                    else:
                        return render(request, 'issue.html', {"form":form}, status=400)
                else:
                    form = IssueForm(instance=book)
                    return render(request, 'issue.html',{"form":form})
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")        
def return_book(request, book_id):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        if profile.user_type=='LIB':
            try:
                book = Book.objects.get(pk=book_id)
            except:
                raise Http404('Book Not Found!')
            else:
                book.issued = False
                book.issued_to = None
                book.issue_date = None
                book.save()
                return redirect('hello')
        else:
            return HttpResponseForbidden("You are not authorized to view this.")

@login_required(login_url="/login/")
def view_issued_books(request):
    try:
        profile = Profile.objects.get(user=request.user, user_type='LIB')
    except Exception as e:
        print(e)
        return HttpResponseForbidden("You are not authorized to view this.")
    else:
        books= Book.objects.filter(issued=True)
        return render(request, 'view_issued.html', {'books':books})
       