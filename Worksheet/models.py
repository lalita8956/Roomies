from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.username
    
class Day(models.Model):
    name = models.CharField(max_length=100,choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    
    
    def __str__(self):
        return self.name
    
class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    work_name = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='works')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.work_name
 


