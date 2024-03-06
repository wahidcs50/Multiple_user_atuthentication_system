from .models import Event
from .serializers import EventsSerializer
from rest_framework import generics

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
