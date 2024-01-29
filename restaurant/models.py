from django.db import models

# Create your models here.


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(null=False)
    BookingDate = models.DateField()


    def __str__(self):
        return self.Name
