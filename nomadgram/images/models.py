from django.db import models

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    catption = models.TextField()

class Comment(TimeStampedModel):

    caption = models.TextField()
