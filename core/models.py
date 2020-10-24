from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_type_choices=[
        ('ADM', 'Admin'),
        ('LIB', 'Librarian'),
        ('GST', 'Guest')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    user_type = models.CharField(default='GST',choices=user_type_choices, max_length=3)

    def __str__(self):
        return str(self.user)+"-"+self.user_type

