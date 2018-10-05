from django.db import models

# Create your models here.
class Image(models.Model):
    Image=models.ImageField(upload_to='Images/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)