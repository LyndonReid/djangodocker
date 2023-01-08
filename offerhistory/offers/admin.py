from django.contrib import admin
from .models import Offer, BrandOffer, CarYear, CarMake, CarModel, WhatIPaid

# Register your models here.
admin.site.register(Offer)
admin.site.register(BrandOffer)
admin.site.register(CarYear)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(WhatIPaid)




