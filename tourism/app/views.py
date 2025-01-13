from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
import smtplib
from email.mime.text import MIMEText
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Set up your email parameters
smtp_server = 'smtp.gmail.com'  
port = 587  
sender_email = 'ced08062003@gmail.com'  
password = 'zwqh vkea xisn trsk'  

recipient_email = 'antoniojhancedric@gmail.com'  
subject = 'Hello'
body = 'This is a test email from Python!'

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email


# BOOKING SYSTEM

def home(request):

    return render(request, 'app/index.html')

def resort_detail(request, id):
    resort = get_object_or_404(Resort, id=id)
    rooms = resort.rooms.all()  
    context = {
        'resort': resort,
        'rooms': rooms
    }
    return render(request, 'app/tourist_page.html', context)


def resort(request):
    resorts = Resort.objects.all()  
    falls = Falls.objects.all()
    restaurants = Restaurant.objects.all()
    cultural_attractions = CulturalAttraction.objects.all()
    context = {
        'resorts': resorts,
        'falls': falls,
        'restaurants': restaurants,
        'cultural_attractions': cultural_attractions
    }
    return render(request, 'app/resort.html', context)


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save()
            selected_resort = form.cleaned_data['resort_name'] 
            name = form.cleaned_data['name'] 
            phone = form.cleaned_data['phone'] 
            gmail = form.cleaned_data['gmail'] 
            room = form.cleaned_data['room'] 
            adult = form.cleaned_data['number_of_adults'] 
            minors= form.cleaned_data['number_of_children'] 
            checkin = form.cleaned_data['checkin_date'] 
            checkout = form.cleaned_data['checkout_date'] 
            resort_instance = Resort.objects.get(id=selected_resort.id) 

            recipient_email = f'{resort_instance.gmail}'  
            subject = 'Booking Confirmation'
            body = f"""
                Name: {name}
                Phone: {phone}
                Email Address: {gmail}
                Commodity: {room}
                Adults: {adult}
                Children: {minors}
                Check-In Date: {checkin}
                Check-Out Date: {checkout}
            """

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient_email

            try:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls()  
                    server.login(sender_email, password)  
                    server.sendmail(sender_email, recipient_email, msg.as_string())  
                print("Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {e}")
            print(resort_instance.gmail)

            return redirect('resort')  

    else:
        form = BookingForm()  

    return redirect('resort')

def form(request, resort_name, room_id):

    resort = get_object_or_404(Resort, name=resort_name)
    room = get_object_or_404(Room, id=room_id)  
    initial_data = {
        'resort_name': resort.id, 
        'room': room.id,            
    }
    form = BookingForm(initial=initial_data)

    return render(request, 'app/form.html', {'form': form, 'resort': resort})

# BOOKING SYSTEM END



# AUTHENTICATIONS
def loginForm(request):
    if request.user.is_authenticated:
        return redirect('auth_home')
    return render(request, 'app/auth/loginForm.html')

def login_view(request):
    print('form activated')
    if request.user.is_authenticated:
        return redirect("auth_home")  
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("auth_home")
        else:
            messages.error(request, "Invalid username or password.")
    return redirect('loginForm')

def logout_view(request):
    logout(request)
    return redirect("loginForm")

def registerForm(request):
    if request.user.is_authenticated:
        return redirect('auth_home')
    form = CustomUserCreationForm()
    return render(request, 'app/auth/registerForm.html', {'form':form})

def create_user_view(request):
    if request.user.is_authenticated:
        return redirect('auth_home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('loginForm') 
        else:
            messages.error(request, "Username or email already exists")
    else:
        form = CustomUserCreationForm()
    
    return redirect('registerForm')

# AUTHENTICATION END

# OWNER PAGE

"""
NAVIGATIONS
- Functions that renders pages
"""
@login_required
def auth_home(request):
    resort = Resort.objects.get(owner=request.user)
    bookings = Booking.objects.filter(resort_name=resort.id)
    return render(request, 'app/auth/booking.html', {'bookings': bookings})

@login_required
def room_page(request):
    resort, created = Resort.objects.get_or_create(owner=request.user)
    rooms = Room.objects.filter(resort=resort)
    
    if request.method == 'POST':
        form = ResortSettingsForm(request.POST, request.FILES, instance=resort)
        room_form = RoomForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            resort_instance = form.save(commit=False)
            resort_instance.owner = request.user  
            resort_instance.save()
            messages.success(request, "Resort settings updated successfully.")
        else:
            messages.error(request, "There was an error updating the resort settings.")
    else:
        form = ResortSettingsForm(instance=resort)
        room_form = RoomForm()  

    context = {
        'form': room_form,
        'rooms': rooms,
    }
    return render(request, 'app/auth/room.html', context)

@login_required
def resort_settings(request):
    resort, created = Resort.objects.get_or_create(owner=request.user)
    rooms = Room.objects.filter(resort=resort)
    
    if request.method == 'POST':
        form = ResortSettingsForm(request.POST, request.FILES, instance=resort)
        room_form = RoomForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            resort_instance = form.save(commit=False)
            resort_instance.owner = request.user  
            resort_instance.save()
            messages.success(request, "Resort settings updated successfully.")
        else:
            messages.error(request, "There was an error updating the resort settings.")
    else:
        form = ResortSettingsForm(instance=resort)
        room_form = RoomForm()  

    context = {
        'form': form,
        'room_form': room_form,
        'rooms': rooms,
    }
    return render(request, 'app/auth/base.html', context)

@login_required
def update_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('resort_settings')  
    else:
        form = RoomForm(instance=room)
    
    return render(request, 'app/auth/roomForm.html', {'form': form})

"""
 END OF NAVIGATIONS
"""

"""
 AUTH PAGES FUNCTIONS
"""
@login_required
def add_room_view(request):
    resort = Resort.objects.get_or_create(owner=request.user)[0] 

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.resort = resort 
            room.save() 
            messages.success(request, "Room added successfully!")
        else:
            print("Form errors:", form.errors)
    else:
        form = RoomForm()

    return redirect('room_page')

@login_required
def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    room.delete()
    messages.success(request, "Room successfully deleted.")
    return redirect('room_page')
"""
 END OF AUTH PAGES FUNCTIONS
"""
# OWNER PAGE END

def festivals(request):
    festivals = Festival.objects.all().order_by('date')
    context = {
        'festivals': festivals
    }
    return render(request, 'app/festivals.html', context)

def events(request):
    events = Event.objects.all().order_by('schedule')
    context = {
        'events': events
    }
    return render(request, 'app/events.html', context)

def activities(request):
    activities = Activity.objects.all().order_by('name')
    context = {
        'activities': activities
    }
    return render(request, 'app/activities.html', context)

def fiestas(request):
    # Order by the day and month of the date field
    fiestas = Fiesta.objects.all().extra(
        select={'month_day': "strftime('%%m-%%d', date)"}
    ).order_by('month_day')
    context = {
        'fiestas': fiestas
    }
    return render(request, 'app/fiestas.html', context)

def cultural_attractions(request):
    attractions = CulturalAttraction.objects.all().order_by('name')
    context = {
        'cultural_attractions': attractions
    }
    return render(request, 'app/cultural_attractions.html', context)
