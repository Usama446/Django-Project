from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return 'Message From ' + self.name + ' From Email ' + self.email