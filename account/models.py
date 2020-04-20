from django.db import models

from django.conf import settings


# Create your models here.
# Error 
#https://stackoverflow.com/questions/26651688/django-integrity-error-unique-constraint-failed-user-profile-user-id
# models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Profile(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
