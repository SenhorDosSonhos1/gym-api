from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class RoleChoices(models.TextChoices):
    ADMIN = "A", "Admin"
    PERSONAL = "P", "Personal"
    MEMBER = "M", "Member"

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # Is active in User
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=RoleChoices.choices, default=RoleChoices.MEMBER)
    photo = models.ImageField(upload_to="media", blank=True, null=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    objective = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.user.email} ({self.role})'
    
