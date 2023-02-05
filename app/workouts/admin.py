from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    ordering = ('timestamp',)
    search_fields = ('title',)

admin.site.register(Workout, WorkoutAdmin)
