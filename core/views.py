from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser as User, Event
from .forms import ProfileUpdateForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            username = username.strip().lower()
        else:
            messages.error(request, 'Username is required!')
            return render(request, 'registration.html')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        year_of_study = request.POST.get('year-of-study')
        role = request.POST.get('role')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'username not availble!')
            return render(request, 'registration.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used!')
            return render(request, 'registration.html')
        else:

            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, phone=phone, department=department, year=year_of_study)
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    
    
    return render(request, 'registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request, 'User not found!')
            return render(request, 'login.html')
        else:
            if user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid password!')
                return render(request, 'login.html')
    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.method == 'POST':
        user = request.user
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        form.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'user': request.user, 'form':form})

def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('profile')
            else:
                messages.error(request, 'Passwords do not match!')
                return render(request, 'change_password.html')
        else:
            messages.error(request, 'Invalid password!')
            return render(request, 'change_password.html')


# create a new view function called events
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


# event detail view function

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, 'event_detail.html', {'event': event})
