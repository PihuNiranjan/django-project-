from django.db import models

# makemigrations : create changes and store in a file
# migrate : apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=250)
    date = models.DateField()
    
    def __str__(self):
        return self.name
