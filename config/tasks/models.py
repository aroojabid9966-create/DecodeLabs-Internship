from django.db import models 
class Task(models.Model):
    STATUS_CHOICES=[
        ('Pending', 'pending'),
        ('Completed', 'completed'),
        ('In_Progress', 'in_progress'),
    ]
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=50,
                            choices=STATUS_CHOICES,
                            default='pending'
                            )
    due_date=models.DateField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
