from django.db import models

class Meme(models.Model):
  name = models.CharField(max_length=100)
  caption = models.TextField(max_length=200)
  url = models.TextField()

  def _str_(self):
    return self.name
