from django.db.models import *
from django.db import models

class Offer(Model):
    Name = TextField()
    Price = IntegerField(default='0')
    def __str__(self):
        return 'Offer: {}'.format(self.Name)

class Barber(Model):
    Name = TextField()
    def __str__(self):
        return 'Barber: {}'.format(self.Name)

class Reservation(Model):
    Offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    Barber = models.ForeignKey(Barber, on_delete=models.CASCADE, null=True)
    Client = TextField()
    Date = DateTimeField()
    def __str__(self):
        return 'Reservation: {}'.format(self.Date) + ' | {}'.format(self.Barber) + ' | Client: {}'.format(self.Client)

