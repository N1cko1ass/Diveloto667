from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.CharField('User`s email', max_length=50)
    username = models.CharField('User`s username', max_length=50)
    password = models.CharField('User`s password', max_length=50)

    class Meta:
        verbose_name = 'SignUp'
        verbose_name_plural = 'SignUp'


    def __str__(self):
        return self.title