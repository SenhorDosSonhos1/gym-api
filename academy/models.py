from django.db import models
from accounts.models import Profile
from django.conf import settings
from datetime import timedelta

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
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT, related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=1, choices=GymPlan.choices, default=GymPlan.MONTHLY)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.profile.user.email} | Plano: {self.plan}'
    
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        ordering = ["status"]
        
class Exercise(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    muscle_group = models.CharField(max_length=12, choices=MuscleGroup.choices)
    photo = models.ImageField(upload_to="exercise/", null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering = ["-created_at"]

class Workout(models.Model):
    name = models.CharField(max_length=155, null = False, blank= False)
    personal = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="workouts")
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'
        ordering = ["-created_at"]

class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name= "workout_exercises")
    series = models.IntegerField(default=1)
    repetitions = models.IntegerField(default=1)
    rest = models.DurationField(default = timedelta(seconds=30), help_text="Tempo de descanso (Ex: 30 segundos ou 2 minutos)")
    order = models.PositiveSmallIntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="Treino")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exercise.name} | {self.series} | {self.repetitions}"
    
    class Meta:
        verbose_name = 'Exercicio do Treino'
        verbose_name_plural = 'Exercicios do Treino'
        ordering = ["order"]