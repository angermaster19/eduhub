from django.shortcuts import render, get_object_or_404
from .models import Batch, Chapter, Lecture

def index(request):
    batches = Batch.objects.all()
    return render(request, "index.html", {'batches': batches})

def neet(request, slug):
    subject = get_object_or_404(Batch, slug=slug)
    chapters = subject.chapters.all()
    return render(request, 'neet.html', {'subject': subject, 'chapters': chapters})

def chapter_list(request, slug):
    subject = get_object_or_404(Batch, slug=slug)
    chapters = subject.chapters.all()
    return render(request, 'chapter_list.html', {'subject': subject, 'chapters': chapters})

def lect(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    lectures = chapter.lectures.all()
    return render(request, 'lecture.html', {'chapter': chapter, 'lectures': lectures})

def lecture_detail(request, slug):
    lecture = get_object_or_404(Lecture, slug=slug)
    return render(request, 'lecture_detail.html', {'lecture': lecture})