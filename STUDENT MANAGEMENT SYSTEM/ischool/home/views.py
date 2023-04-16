from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('login_page')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('home')
    return render(request, 'login_page.html')

@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('login_page')



@login_required(login_url='login_page')
def home(request):
    if request.method =="POST":
        data = request.POST
        student_image = request.FILES.get('student_image')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        about = data.get('about')
        address = data.get('address')
        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            address = address,
            about = about,
            student_image = student_image,
        )
        return redirect('home')

    return render(request, 'home.html')

@login_required(login_url='login_page')
def dashboard(request):
    queryset = Student.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(first_name__icontains = request.GET.get('search'))
    
    context = {'students':queryset}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login_page')
def delete_student(request, id):
    queryset = Student.objects.get(id = id)
    queryset.delete()
    return redirect('dashboard')  

@login_required(login_url='login_page')
def update_student(request, id):
    queryset = Student.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        student_image = request.FILES.get('student_image')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        about = data.get('about')
        address = data.get('address')

        queryset.first_name = first_name
        queryset.last_name =last_name
        queryset.phone = phone
        queryset.email = email
        queryset.about = about
        queryset.address = address


        if student_image:
            queryset.student_image = student_image
        
        queryset.save()   
        return redirect('dashboard')

    context = {'student':queryset}

    return render(request, 'update.html', context)