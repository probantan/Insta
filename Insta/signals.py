# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from Insta.models import Profile


# @receiver(post_save,sender=User)
# def create_profile(created, instance, sender,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save,sender=User)
# def save_profile( instance, sender,**kwargs):
#     instance.profile.save()
            
