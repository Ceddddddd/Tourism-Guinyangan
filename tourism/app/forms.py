from django import forms
from .models import Booking, Resort, Room

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
