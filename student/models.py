from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    computer_science = models.IntegerField()

    def __str__(self):
        return self.name