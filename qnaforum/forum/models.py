from django.db import models

# Create your models here.

class Forum(models.Model):
    name = models.CharField(max_length=30)
    ans = models.TextField()
    quest = models.TextField()

class Questions(models.Model):
    quest_num = models.ForeignKey(Forum, models.CASCADE)
    quest_content = models.TextField()
    quest_id = models.TextField()
