from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade = if user deleted, delete profile
    #instantiating profile pic field, default image, images uploaded to profile_pic directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') 


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            #resize
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)



