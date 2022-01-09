from django.contrib import admin

from app.models import Offer
admin.site.register(Offer)

from app.models import Reservation
admin.site.register(Reservation)

from app.models import Barber
admin.site.register(Barber)