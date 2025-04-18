from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from core.models import Event, CustomUser as User, Testimony
from .forms import EventForm, TestimonyForm


# dashboard views
def dashboard_home(request):
    users = User.objects.all()
    events = Event.objects.all()
    return render(request, 'dashboard/index.html', {'users': users, 'events': events})

# event detail by slug
def event_detail(request, event_id):
    
    return render(request, 'dashboard/event_detail.html')


def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        cover_p = request.FILES.get('cover_p')
        attendees = request.POST.getlist('attendees')
        event = Event(title=title, time=time, date=date, location=location, description=description, cover_p=cover_p)
        event.save()
        event.attendees.set(attendees)

        return JsonResponse({'status': 'success', 'message': 'Event created successfully'})
    return render(request, 'dashboard/create_event.html')

# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Event created successfully')
#             return redirect('events_list')
#         else:
#             for field in form:
#                 for error in field.errors:
#                     messages.error(request, f'{field.label}: {error}')
#                     return render(request, 'dashboard/create_event.html', {'form': form})
        
    
# update event
def update_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('events_list')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f'{field.label}: {error}')
                    return render(request, 'dashboard/update_event.html', {'form': form})
    else:
        form = EventForm(instance=event)
    return render(request, 'dashboard/update_event.html', {'form': form})

# delete event
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully')
    return redirect('events_list')

# events list
def events_list(request):
    events = Event.objects.all()

    # event = Event.objects.filter(id=)
    return render(request, 'dashboard/events.html', {'events': events})


# admin profile
def admin_profile(request):

    return render(request, 'dashboard/profile.html')


def create_user(request):
    if request.user.is_superuser:
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
            is_admin = request.POST.get('is_admin')


            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': 'username not availble!'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'Email already used!'})
            else:
                if is_admin:
                    user = User.objects.create_superuser(username=username, first_name=first_name, last_name=last_name, email=email, password=password, phone=phone, department=department, year=year_of_study)
                else:
                    
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, phone=phone, department=department, year=year_of_study)
                user.save()
                messages.success(request, 'User created successfully!')
                return redirect('users_list')
        else:
            return render(request, 'dashboard/users.html')
    else:
        messages.error(request, 'Access denied!')
        return redirect('home')


def users_list(request):
    users = User.objects.all()
    return render(request, 'dashboard/users.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'dashboard/user_detail.html', {'user': user})

def update_user(request, user_id):
    # update and return jsonresponse instead of refreshing the page
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        year_of_study = request.POST.get('year_of_study')
        is_admin = request.POST.get('is_admin')
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        user.department = department
        user.year = year_of_study
        if is_admin:
            user.is_superuser=True
        else:
            user.is_superuser=False
        user.save()
        return JsonResponse({'status': 'success', 'message': 'User updated successfully!'})
def delete_user(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        user.delete()
        messages.success(request, 'account deleted!')
        return redirect('users_list')
    
    except Exception as e:
        messages.error(request, f'request failed, error: {e}')
        return redirect('users_list')

def testimonies_list(request):
    testimonies = Testimony.objects.all().order_by('-date')
    return render(request, 'dashboard/testimonies_list.html', {'testimonies': testimonies})

def new_testimony(request):
    if request.method == 'POST':
        user = request.user
        if user:
            form = TestimonyForm(request.POST, request.FILES)
            if form.is_valid():
                testimony = form.save(commit=False)
                testimony.user = user
                testimony.save()
        else:
            form = TestimonyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        messages.success(request, 'New testimony added!')
        return redirect('testimonies_list')
    else:
        form = TestimonyForm()
        return render(request, 'dashboard/create_testimony.html', {'form':form})

def approve_testimony(request, pk):
    try:
        testimony = get_object_or_404(Testimony, id=pk)
        testimony.is_approved = True
        testimony.save()
        messages.success(request, 'Testimony approved successfully!')
    except Exception as e:
        messages.error(request, f'Failed to approve testimony: {e}')
    return redirect('testimonies_list')


def update_testimony(request, pk):
    testimony = get_object_or_404(Testimony, id=pk)
    if request.method == 'POST':
        form = TestimonyForm(request.POST, request.FILES, instance=testimony)
        if form.is_valid():
            form.save()
            messages.success(request, 'testimony updated!')
            return redirect('testimonies_list')
        else:
            messages.error(request, 'Failed to update testimony!')
            return render(request, 'dashboard/testimony_update.html')
    else:
        form = TestimonyForm(instance=testimony)
    return render(request, 'dashboard/testimony_update.html', {'form': form, 'testimony': testimony})

def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, id=pk)
    return render(request, 'dashboard/testimony_detail.html', {'testimony': testimony})

def delete_testimony(request, pk):
    testimony = get_object_or_404(Testimony, id=pk)
    testimony.delete()
    messages.success(request, 'Testimony deleted!')
    return redirect('testimonies_list')


        


    





