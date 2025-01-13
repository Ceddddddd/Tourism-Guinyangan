from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Resort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    entrance_fee_adult = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    entrance_fee_discounted = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone = models.CharField(max_length=15)
    gmail = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    
    # Add a ForeignKey to CustomUser for the owner relationship
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resorts')

    def __str__(self):
        return self.name



class Room(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE, related_name='rooms')
    picture = models.ImageField(upload_to='app/images/', blank=True)
    description = models.TextField(blank=True, null=True)
    room_name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start = models.TimeField()
    finish = models.TimeField()
    entrance = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.resort.name}'s {self.room_name}"


class Booking(models.Model):
    resort_name = models.ForeignKey(Resort, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    number_of_adults = models.PositiveIntegerField()
    number_of_children = models.PositiveIntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  
    phone = models.CharField(max_length=15)
    gmail = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"Booking at {self.resort_name.name} from {self.checkin_date} to {self.checkout_date}"


class Falls(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app/images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=100)
    price_range = models.CharField(max_length=50)
    facebook = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class CulturalAttraction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)  
    historical_significance = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='app/images/', blank=True, null=True)
    visiting_hours = models.CharField(max_length=100, blank=True, null=True)
    entrance_fee = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True, null=True)
    cultural_practices = models.TextField(blank=True, null=True)  # Local customs and practices
    image_url = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    cultural_significance = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    schedule = models.DateTimeField()
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    organizer = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)  # e.g., "2 hours", "Half day"
    difficulty_level = models.CharField(max_length=20, blank=True, null=True)  # e.g., "Easy", "Moderate", "Difficult"


    def __str__(self):
        return self.name

class Fiesta(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()  # Annual celebration date
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    patron_saint = models.CharField(max_length=255, blank=True, null=True)  # For religious fiestas
    traditional_food = models.TextField(blank=True, null=True)  # Traditional foods served

    def __str__(self):
        return self.name
