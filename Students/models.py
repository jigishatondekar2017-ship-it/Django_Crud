from django.db import models

# Create your models here.
class Student(models.Model):
    rno=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    fees=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name