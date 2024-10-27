from django.shortcuts import render,redirect
from .forms import BookingForm
from .models import *
from django.shortcuts import render, get_object_or_404
import smtplib
from email.mime.text import MIMEText

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