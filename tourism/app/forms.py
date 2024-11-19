from django import forms
from .models import Booking, Resort, Room, CustomUser  

from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['resort_name', 'checkin_date', 'checkout_date', 'number_of_adults', 'number_of_children','name', 'room', 'phone','gmail']
        widgets = {
            'resort_name': forms.Select(attrs={'class': 'form-control'}),
            'checkin_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'checkout_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number_of_adults': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_children': forms.NumberInput(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gmail': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # You can also customize the queryset for the dropdowns if needed
    resort_name = forms.ModelChoiceField(queryset=Resort.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    room = forms.ModelChoiceField(queryset=Room.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser  
        fields = ["username", "email", "first_name" , "last_name" , "password1", "password2"]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ResortSettingsForm(forms.ModelForm):
    class Meta:
        model = Resort
        fields = [
            'name', 'description', 'entrance_fee_adult', 'entrance_fee_discounted',
            'phone', 'gmail', 'facebook', 'location',
            'image_1', 'image_2', 'image_3', 'image_4', 'image_5'
        ]
        
        # Widgets with Bootstrap styling
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resort Name'}),  # Bootstrap form-control for text input
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),  # Bootstrap form-control for textarea
            'entrance_fee_adult': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01, 'placeholder': 'Entrance Fee for Adults'}),  # Bootstrap form-control for number input
            'entrance_fee_discounted': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01, 'placeholder': 'Discounted Entrance Fee'}),  # Same as above for discounted fee
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),  # Bootstrap form-control for phone input
            'gmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),  # Email input field with Bootstrap styling
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook Link'}),  # Bootstrap form-control for facebook link
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),  # Bootstrap form-control for location
            
            # Custom styling for image fields to remove unwanted design
            'image_1': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),  # Adjust image preview design
            'image_2': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),  # Same styling for other images
            'image_3': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),
            'image_4': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),
            'image_5': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'picture', 'description', 'capacity', 'price', 'start', 'finish', 'entrance']
        widgets = {
            'room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room name'}),
            'start': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Select start time'}),
            'finish': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Select finish time'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter room price'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Enter room capacity'}),
            'entrance': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Enter entrance fee'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload room image'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter room description'}),
        }
        labels = {
            'room_name': 'Room Name',
            'capacity': 'Capacity',
            'price': 'Price',
            'start': 'Start Time',
            'finish': 'Finish Time',
            'entrance': 'Entrance Fee',
            'description': 'Description',
            'picture': 'Room Picture',
        }