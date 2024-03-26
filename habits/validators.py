from rest_framework import serializers


def validator_exclude_award_and_related_habit(value):
    award = value.get('award')
    related_habit = value.get('related_habit')

    if award and related_habit:
        raise serializers.ValidationError(
            'Simultaneous selection of a related habit and indication of a reward is prohibited')


def validator_time_to_complete(value):
    max_time = 120
    if value > max_time:
        raise serializers.ValidationError(f'The execution time should be no more than {max_time} seconds')


def validator_related_habit(value):
    if not value.is_pleasant:
        raise serializers.ValidationError('A related habit should have the hallmark of a pleasant habit')


def validator_not_award_or_related_habit(value):
    is_pleasant = value.get('is_pleasant')
    award = value.get('award')
    related_habit = value.get('related_habit')

    if is_pleasant and (award or related_habit is not None):
        raise serializers.ValidationError('A pleasant habit cannot have a reward or a related habit.')


def validator_frequency(value):
    max_frequency = 7
    if value > max_frequency:
        raise serializers.ValidationError(f'You should not perform the habit less than once every {max_frequency} days')