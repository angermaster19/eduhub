from django.db import models
from django.utils.text import slugify

class Batch(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title 

class Chapter(models.Model):
    subject = models.ForeignKey(Batch, related_name='chapters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name 
    
# p
    
class Lecture(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    video = models.FileField(upload_to='videos/')
    pdf = models.CharField(max_length=10000)
    # dpp = models.CharField(max_length=10000)

    def __str__(self):
        return self.title

