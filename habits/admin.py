from django.contrib import admin

from habits.models import Habit, Award


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'award', 'place', 'execution_time', 'action', 'is_pleasant', 'related_habit', 'frequency',
        'time_to_complete', 'is_published',)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'reward',)
