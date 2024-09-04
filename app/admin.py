# notes/admin.py

from django.contrib import admin
from .models import Note, Batch , Chapter, Lecture

admin.site.register(Note)
admin.site.register(Batch)
admin.site.register(Chapter)
admin.site.register(Lecture)
