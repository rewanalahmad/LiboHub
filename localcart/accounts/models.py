from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,
                              related_name="profile")
    bio=models.TextField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now=True,null=True)
    photo=models.ImageField(upload_to="profile_photos/",null=True,blank=True)

    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def create_or_update_userprofile(sender,instance,created,**args):
    """
    when u create a user this function checks if this is new creater instanc,
    if it's true the he go and create userprofile 
    """
    if created :
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()