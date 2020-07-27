from django.urls import path

from .views import (
		NotesListView,
		NoteCreateView,
		ComposerPageView
	)


urlpatterns = [
	path('', NotesListView.as_view(), name='notes'),
	path('composer/', ComposerPageView.as_view(), name='composer' ),
	path('new/', NoteCreateView.as_view(), name='create')
]
