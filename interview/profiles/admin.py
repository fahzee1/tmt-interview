from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_admin')
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(UserProfile, UserProfileAdmin)
