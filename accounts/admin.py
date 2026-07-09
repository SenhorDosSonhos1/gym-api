from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["get_user_email", "role"]
    search_fields = ["role"]
    ordering = ["created_at"]

    @admin.display(
            empty_value="???"
    )
    def get_user_email(self, obj):
        if not obj:
            return None
        return obj.user.email
    
    