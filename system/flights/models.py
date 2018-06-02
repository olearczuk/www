"""models module"""
from django.db import models


class Passenger(models.Model):
    """Passenger class"""
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'surname')


class Airplane(models.Model):
    """Airplane class"""
    capacity = models.IntegerField(default=25)
    official_number = models.CharField(max_length=100, primary_key=True)


class Airport(models.Model):
    """Airport class"""
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        unique_together = ('country', 'city')


class Flight(models.Model):
    """Flight class"""
    start_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,
                                      related_name='start_airport')
    departure_time = models.DateTimeField()

    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='airplane')
    passengers = models.ManyToManyField(Passenger, through='Ticket')

    final_airport = models.ForeignKey(Airport, on_delete=models.CASCADE,
                                      related_name='final_airport')
    arrival_time = models.DateTimeField()


class Ticket(models.Model):
    """Ticket class"""
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)


class Crew(models.Model):
    captainsName = models.CharField(max_length=150)
    captainsSurname = models.CharField(max_length=150)
    flights = models.ManyToManyField(Flight, related_name='crew', through='Contract')

    class Meta:
        unique_together = ('captainsName', 'captainsSurname')


class Contract(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)