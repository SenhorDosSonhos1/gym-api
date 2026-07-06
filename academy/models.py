from django.db import models
from accounts.models import Profile

class GymPlan(models.TextChoices):
    MONTHLY = "M", "Mensal"
    QUARTERLY = "T", "Trimestral"
    SEMIANNUAL = "S", "Semestral"

class MuscleGroup(models.TextChoices):
    CHEST = "PE", "Peito"
    BACK = "C", "Costas"
    SHOULDERS = "O", "Ombros"
    ARMS = "B", "Braços"
    LEGS = "P", "Pernas"
    GLUTES = "G", "Gluteos"
    CORE = "A", "Abdômen"

class Membership(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=1, choices=GymPlan.choices, default=GymPlan.MONTHLY)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'Nome: {self.profile.user.email} | Plano: {self.plan}'
    
class Exercise(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    muscle_group = models.CharField(max_length=12, choices=MuscleGroup.choices)
    photo = models.ImageField(upload_to="exercise/", null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Exercicio: {self.name} | Parte: {self.muscle_group}"