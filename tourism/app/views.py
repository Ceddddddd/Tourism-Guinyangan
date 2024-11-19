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
smtp_server = 'smtp.gmail.com'  # or your SMTP server
port = 587  # For TLS
sender_email = 'ced08062003@gmail.com'  # Replace with your email
password = 'zwqh vkea xisn trsk'  # Replace with your email password

recipient_email = 'antoniojhancedric@gmail.com'  # Replace with recipient's email
subject = 'Hello'
body = 'This is a test email from Python!'

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email


def home(request):

    return render(request, 'app/index.html')

# Details of selected Resort
def resort_detail(request, id):
    resort = get_object_or_404(Resort, id=id)
    rooms = resort.rooms.all()  # Fetch only rooms associated with the specified resort
    context = {
        'resort': resort,
        'rooms': rooms
    }
    return render(request, 'app/tourist_page.html', context)

# Redirect to List of resorts 
def resort(request):
    resorts = Resort.objects.all()  
    context = {'resorts': resorts}  
    return render(request, 'app/resort.html', context)

# Handles form submission
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

            # Sends an email
            recipient_email = f'{resort_instance.gmail}'  # Replace with recipient's email
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

            # Create the email message
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

# Goes to the Form page 
def form(request, resort_name, room_id):

    resort = get_object_or_404(Resort, name=resort_name)
    room = get_object_or_404(Room, id=room_id)  
    initial_data = {
        'resort_name': resort.id, 
        'room': room.id,            
    }
    form = BookingForm(initial=initial_data)

    return render(request, 'app/form.html', {'form': form, 'resort': resort})



def loginForm(request):
    return render(request, 'app/auth/loginForm.html')

def login_view(request):
    print('form activated')
    if request.user.is_authenticated:
        return redirect("resort_settings")  # Redirect logged-in users
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("resort_settings")
        else:
            messages.error(request, "Invalid username or password.")
    return redirect('loginForm')

def logout_view(request):
    logout(request)
    return redirect("loginForm")

def registerForm(request):
    form = CustomUserCreationForm()
    return render(request, 'app/auth/registerForm.html', {'form':form})


def create_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('loginForm')  # Redirect to the login page or another relevant page
        else:
            messages.error(request, "Username or email already exists")
    else:
        form = CustomUserCreationForm()
    
    return redirect('registerForm')

@login_required
def resort_settings(request):
    # Fetch the first resort or create a new one if it doesn't exist
    resort, created = Resort.objects.get_or_create(owner=request.user)
    
    # Fetch all room instances related to this resort for display
    rooms = Room.objects.filter(resort=resort)
    
    if request.method == 'POST':
        # Resort form handling
        form = ResortSettingsForm(request.POST, request.FILES, instance=resort)
        room_form = RoomForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            resort_instance = form.save(commit=False)
            resort_instance.owner = request.user  # Ensure the owner is set
            resort_instance.save()
            messages.success(request, "Resort settings updated successfully.")
        else:
            messages.error(request, "There was an error updating the resort settings.")
    else:
        form = ResortSettingsForm(instance=resort)
        room_form = RoomForm()  # Blank form for adding new rooms

    context = {
        'form': form,
        'room_form': room_form,
        'rooms': rooms,
    }
    return render(request, 'app/auth/base.html', context)

@login_required
def add_room_view(request):
    # Get or create a resort instance for the current user
    resort = Resort.objects.get_or_create(owner=request.user)[0]  # This assumes the Resort model has a ForeignKey to User as 'owner'

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the room and associate it with the resort
            room = form.save(commit=False)
            room.resort = resort  # Automatically associate the room with the resort
            room.save()  # Save the room instance
            messages.success(request, "Room added successfully!")
            return redirect('resort_settings')  # Adjust this to wherever you want to redirect after adding a room
        else:
            print("Form errors:", form.errors)
    else:
        form = RoomForm()

    return redirect('resort_settings')

@login_required
def update_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('resort_settings')  # Redirect to a room list or detail view after updating
    else:
        form = RoomForm(instance=room)
    
    return render(request, 'app/auth/roomForm.html', {'form': form})

@login_required
def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    room.delete()
    messages.success(request, "Room successfully deleted.")
    return redirect('resort_settings')
