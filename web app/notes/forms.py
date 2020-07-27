from django import forms

from .models import Note


class UserNoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title', ]
		