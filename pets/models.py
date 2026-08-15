from django.db import models
class Pet(models.Model):
    STATUS_CHOICES=[
        ('Available','available'),
        ('Adopted','adopted'),
    ]
    GENDER_CHOICES=[
        ('Male','male'),
        ('Female','female'),
    ]
    name=models.CharField(max_length=100)
    species=models.CharField(max_length=50)
    breed=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=50, choices=GENDER_CHOICES)
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    def __str__(self):
        return self.name
    

                            
