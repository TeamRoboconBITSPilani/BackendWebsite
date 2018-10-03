from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey("auth.User")
    title=models.Charfield(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=False)

    
