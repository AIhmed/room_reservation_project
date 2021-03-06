from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Room(models.Model):
    room_number = models.IntegerField()
    floor = models.SmallIntegerField()

    def __repr__(self):
        return f'Room {self.room_number} floor {self.floor}'


class Reservation(models.Model):
    PRICES = {
            '1': 5000.00,
            '2': 9000.00,
            '3': 14000.00,
            '4': 18000.00,
            '5': 21000.00,
            '6': 25000.00,
            '7': 28000.00
            }
    NUM_DAYS = [('1', 'one day'), ('2', 'two days'), ('3', 'three days'), ('4', 'four days'), ('5', 'five days')]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    number_days = models.CharField(max_length=1, null=True, blank=False, choices=NUM_DAYS)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    # we need to add a function for post processing to get an estimated price if number_day is not null

    def save(self, *args, **kwargs):
        if self.number_days is not None:
            self.price = self.PRICES[str(self.number_days)]
        else:
            self.price = 5000.0
            self.number_days = '1'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detailreservation', {'pk': self.pk})

    def __repr__(self):
        return f'Reservation number {self.pk}'


# for foreign keys


'''
Customer - Order : a Customer can have multiple Orders

that mean that we will be creating an order using a customer. each time we create an order we can have the same customer making a that order but the same order with it's own Id will never be ordered by multiple customer.
'''
