from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.username

class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    Work_name = models.TextField()
    day = models.CharField(default=None, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.Work_name
 


