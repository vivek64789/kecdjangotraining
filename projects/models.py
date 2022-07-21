from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    featured_img = models.CharField(max_length=1000, null=True, blank=True)
    vote_ratio = models.CharField(max_length=1000, null=True, blank=True)
    vote_count = models.CharField(max_length=1000, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    VOTE_TYPE = (('up', 'Up Vote'), ('down', 'Down Vote'))
    #user
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    body = models.TextField(null=True, blank=False)
    value = models.CharField(max_length=200, choices= VOTE_TYPE)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.body

    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
