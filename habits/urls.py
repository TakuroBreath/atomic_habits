from django.urls import path

from habits.api_views.habit import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitPublicListAPIView
from habits.api_views.award import AwardListAPIView, AwardCreateAPIView, AwardUpdateAPIView, AwardDestroyAPIView
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/list/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/list/public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),

    path('award/list/', AwardListAPIView.as_view(), name='award_list'),
    path('award/create/', AwardCreateAPIView.as_view(), name='award_create'),
    path('award/update/<int:pk>/', AwardUpdateAPIView.as_view(), name='award_update'),
    path('award/delete/<int:pk>/', AwardDestroyAPIView.as_view(), name='award_delete'),
]
