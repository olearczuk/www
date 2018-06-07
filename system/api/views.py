from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import *


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.order_by("-departure_time")
    serializer_class = FlightSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # TODO select_for_update
        crew_id = request.data['crew']
        crew_flights = Flight.objects.filter(crew=crew_id, departure_time__lte=instance.arrival_time,
                                             arrival_time__gte=instance.departure_time)
        if crew_flights.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)