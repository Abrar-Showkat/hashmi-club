from django.db import models
from datetime import date

class Player(models.Model):
    img=models.ImageField(upload_to='club/images/')
    name=models.CharField(max_length=20)
    jersey=models.IntegerField()
    matches=models.IntegerField()
    position=models.CharField(max_length=20)
    instaurl=models.URLField(blank=True)
    fburl=models.URLField(blank=True)
    dob=models.DateField()
    doj=models.DateField()



    def __str__(self):
        return self.name

select = (
    ("won","WON"),
    ("loss","LOSS"),
    ("notplayed","NOTPLAYED"),
)
class Matches(models.Model):
    opposition=models.CharField(max_length=30)
    time=models.TimeField()
    date=models.DateField()
    place=models.CharField(max_length=100)
    result=models.CharField(max_length=20, choices=select, default='NOTPLAYED')
    mygoals=models.IntegerField(null=True, blank=True)
    oppositiongoals=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'vs ' + self.opposition


    def is_date_due(self):
        return date.today()>self.date


class  Image(models.Model):
    homeimage=models.ImageField(upload_to='club/images/')

class Managers(models.Model):
    image=models.ImageField(upload_to='club/images/')
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=40)


    def __str__(self):
        return self.name

    


