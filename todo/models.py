from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class TodoItem(models.Model):
    text = models.TextField()
    todo = models.ForeignKey(Todo)

    def __unicode__(self):
        return self.text
