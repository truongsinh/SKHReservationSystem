__author__ = 'Jussi'
from Parking.models import Area, Type, Slot, Queue, Transaction
from django.contrib import admin

admin.site.register(Area)
admin.site.register(Type)
admin.site.register(Slot)
admin.site.register(Queue)
admin.site.register(Transaction)

