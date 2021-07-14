from django.db import models

# Create your models here.
class Meet(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    about=models.TextField()


    def __str__(self):
         return self.name