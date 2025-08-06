from django.db import models


class Work(models.Model):
    Work_name = models.TextField()
    day = models.CharField(default=None, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.Work_name
 
class Task(models.Model):
    task_name = models.TextField()
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_name


