from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    notes = models.TextField(default = 'Enter Note')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name