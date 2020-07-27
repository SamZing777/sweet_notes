from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Note(models.Model):
	CATEGORIES = (
		('Poem', 'POEM'),
		('Quotes', 'QUOTES'),
		('Word of Wisdom', 'WORD OF WISDOM')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100, help_text='If note is composed by you'
	 													'use your name(optional)',
														blank=True, null=True
	 						)
	body = models.TextField(max_length=1000, default='Who sat and watch my Infantness')
	category = models.CharField(max_length=50, choices=CATEGORIES, default='Poem')
	timeStamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('composer', args=[str(self.id)])


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=200)
	timeStamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)
