from django.db import models

class Resort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    entrance_fee_adult = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    entrance_fee_discounted = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    phone = models.CharField(max_length=15)
    gmail = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='app/images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='app/images/', blank=True, null=True)

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
