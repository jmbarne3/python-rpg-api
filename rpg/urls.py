from django.urls import path

from rpg.views import (
    CharacterDetailView,
    CharacterListView
)

urlpatterns = [
    path(r'characters/<id>/',
        CharacterDetailView.as_view(),
        name='api.characters.detail'
    ),
    path(r'characters/',
        CharacterListView.as_view(),
        name='api.characters.list'
    )
]
