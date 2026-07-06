from django.db import models
from accounts.models import Profile

class GymPlan(models.TextChoices):
    MONTHLY = "M", "Mensal"
    QUARTERLY = "T", "Trimestral"
    SEMIANNUAL = "S", "Semestral"

class Membership(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=1, choices=GymPlan.choices, default=GymPlan.MONTHLY)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'Nome: {self.profile.user.email} | Plano: {self.plan}'