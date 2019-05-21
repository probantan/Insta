from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to='profile/')
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile   


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['-name']

    def save_tag(self):
        self.save()

class Image(models.Model):
    image=models.ImageField(upload_to='Images/')
    likes = models.PositiveIntegerField(default=0)
    caption = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-time'] 

    def save_images(self):
        self.save()

    def total_likes(self):
        return self.likes.count()



class Comment(models.Model):
    text= models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    time_posted = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-time_posted']

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.text


