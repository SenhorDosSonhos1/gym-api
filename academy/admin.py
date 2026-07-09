from django.contrib import admin
from academy.models import Membership, Exercise, Workout, WorkoutExercise

admin.site.register(Membership)
admin.site.register(Exercise)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["name", "get_email_personal", "get_email_member", ]
    search_fields = ["name"]
    ordering = ["name"]

    @admin.display(
       empty_value="???"
    )
    def get_email_member(self, obj):
        if not obj.member.profile.user.email:
            return None
        return f"{obj.member.profile.user.email}"
    
    @admin.display(
       empty_value="???"
    )
    def get_email_personal(self, obj):
        if not obj.personal.user.email:
            return None
        return f"{obj.personal.user.email}"
    
@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ["exercise", "series", "repetitions", "rest"]
    search_fields = ["exercise"]

    
