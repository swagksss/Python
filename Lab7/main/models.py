from django.db import models

class Object(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
