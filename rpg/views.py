from rest_framework import generics

from rpg.models import (
    Character
)

from rpg.serializers import (
    CharacterSerializer
)

# Create your views here.
class CharacterListView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    lookup_field = 'id'
    serializer_class = CharacterSerializer
