"""forms module"""
from django.forms import ModelForm
from .models import Passenger, Flight
from django.contrib.admin import widgets

class PassengerForm(ModelForm):
    """Passenger form"""
    class Meta:
        """Meta class"""
        model = Passenger
        fields = '__all__'


class FlightForm(ModelForm):
    """Flight form"""
    class Meta:
        """Meta class"""
        model = Flight
        fields = ['departure_time', 'arrival_time']

        # def validate(self, value):

    #
    # def __init__(self, *args, **kwargs):
    #     super(FlightForm, self).__init__(*args, **kwargs)
    #     self.fields['departure_time'].widget = widgets.AdminDateWidget()
    #     self.fields['arrival_time'].widget = widgets.AdminDateWidget()
