from django.db import models
from django.contrib.auth import user


class Room(models):
    PRICES = {
            '1': 5000.00,
            '2': 9000.00,
            '3': 14000.00,
            '4': 18000.00,
            '5': 21000.00,
            '6': 25000.00,
            '7':28000.00
            }
    NUM_DAYS = [('1', 'one day'), ('2', 'two days'), ('3', 'three days'), ('4', 'four days'), ('5', 'five days')]
    room_number = models.IntegerField()
    floor = models.SmallIntegerField()
    reservation_date = models.DateTimeField()
    number_days = models.IntegerField(null=True, blank=False, NUM_DAYS, defaut='3')
    client = models.ForeignKey(user, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, max_places=2)
    # we need to add a function for post processing to get an estimated price if number_day is not null

    def save(self, *agrs, **kwargs):
        # map choices from number_days and get the price
        if self.number_days is not None:
            self.price = PRICES[self.number_days]
        super().save(*args, **kwargs)
