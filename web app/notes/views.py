from django.views import generic
from django.urls import reverse_lazy

from .models import Note, Comment
from .forms import UserNoteForm


class NotesListView(generic.ListView):
	model = Note
	context_object_name = 'notes'
	paginate_by = 20
	ordering = ['-timeStamp']
	template_name = 'notes/index.html'


class NoteCreateView(generic.CreateView):
	form_class = UserNoteForm
	success_url = reverse_lazy('index')
	template_name = 'notes/create_note.html'


class ComposerPageView(generic.ListView):
	model = Note
	template_name = 'notes/composer.html'

