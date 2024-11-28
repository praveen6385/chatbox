from django.db import models

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.username}: {self.text[:30]}"