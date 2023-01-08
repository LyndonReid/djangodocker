from django.db import models

# Create your models here.
class Offer(models.Model):
    caryear             = models.PositiveSmallIntegerField(null=False)
    carmake             = models.CharField(max_length=100, null=False)
    carmodel            = models.CharField(max_length=100, null=False)
    cartrim             = models.CharField(max_length=100, null=True)
    offerlocation       = models.CharField(max_length=100, null=False)
    offertype           = models.CharField(max_length=100, null=False)
    offerstartdate      = models.DateField(null=False)
    offerenddate        = models.DateField(null=False)
    financerate         = models.FloatField(null=True)
    financeduration     = models.CharField(max_length=100, null=True)
    leasepayment        = models.FloatField(null=True)
    leaserate           = models.FloatField(null=True)
    leaseduration       = models.CharField(max_length=100, null=True)
    leasedownpayment    = models.FloatField(null=True)
    cashdealincentive   = models.FloatField(null=True)
    offeranddeal        = models.CharField(max_length=100, null=True)
    offerplusdeal       = models.CharField(max_length=100, null=True)
    offerdetailsummary  = models.CharField(max_length=1000, null=True)
    offerdetaildetails  = models.CharField(max_length=10000, null=True)
    offeristackable     = models.BooleanField(null=True)
    offermonth          = models.TextField(null=True)

class BrandOffer(models.Model):
    caryear             = models.PositiveSmallIntegerField(null=False)
    carmake             = models.CharField(max_length=100, null=False)
    offertype           = models.CharField(max_length=100, null=False)
    offerstartdate      = models.DateField(null=False)
    offerenddate        = models.DateField(null=False)
    offerdetailsummary  = models.CharField(max_length=100, null=False)
    offerdetaildetails  = models.CharField(max_length=10000, null=True)
    offeristackable     = models.BooleanField(null=True)
    offermonth          = models.TextField(null=True)

class CarYear(models.Model):
    caryear             = models.IntegerField(null=False)

class CarMake(models.Model):
    carmake             = models.CharField(max_length=100)

class CarModel(models.Model):
    carmake             = models.CharField(max_length=100)
    carmodel            = models.CharField(max_length=100)
    cartype             = models.CharField(max_length=100)

class WhatIPaid(models.Model):
    caryear             = models.ForeignKey(CarYear, on_delete=models.CASCADE)
    carmake             = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    carmodel            = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    carmsrp             = models.FloatField()
    paidpretax          = models.FloatField()
    paidoutthedoor      = models.FloatField()
    comments            = models.CharField(max_length=3000)



