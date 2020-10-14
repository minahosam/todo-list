from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.title
    