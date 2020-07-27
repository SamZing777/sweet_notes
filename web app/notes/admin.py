from django.contrib import admin

from .models import Note, Comment


class NoteAdmin(admin.ModelAdmin):
	list_display = ['title', 'user', 'author', 'category']


admin.site.register(Note, NoteAdmin)


# admin@sweet_notes.com