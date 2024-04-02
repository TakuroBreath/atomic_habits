from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from habits import validators
from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.IntegerField(validators=[validators.validator_time_to_complete])

    periodic = serializers.IntegerField(validators=[validators.validator_periodic])

    parent_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[validators.validator_parent_habit],
        allow_null=True,
        required=False
    )

    user = SlugRelatedField(slug_field='email', queryset=User.objects.all(), required=False)

    telegram_id = serializers.SerializerMethodField()

    def get_telegram_id(self, obj):
        return obj.user.telegram_id if obj.user else None

    class Meta:
        model = Habit
        fields = (
            'pk', 'user', 'award', 'place', 'execution_time', 'action', 'is_pleasant', 'parent_habit', 'periodic',
            'time_to_complete', 'is_public', 'telegram_id',)

        validators = [
            UniqueTogetherValidator(
                queryset=Habit.objects.all(),
                fields=['award', 'parent_habit', 'is_pleasant'],
            ),
            validators.validator_exclude_award_and_parent_habit,
            validators.validator_not_award_or_parent_habit
        ]
