from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.serializers.habit import HabitSerializer
from habits.services import TelegramNotificationBot


@shared_task
def task_send_notification():
    habits = Habit.objects.all()

    now_time = datetime.now().time()

    for habit in habits:
        serializer = HabitSerializer(habit)
        habit_data = serializer.data
        chat_id = habit_data.get('telegram_id')

        habit_execution_time = habit.execution_time

        # Creating datetime objects with the same date, for subsequent subtraction
        now_datetime = datetime.combine(datetime.today().date(), now_time)
        habit_execution_datetime = datetime.combine(datetime.today().date(), habit_execution_time)

        time_difference = habit_execution_datetime - now_datetime

        if 3600 < time_difference.total_seconds() <= 2 * 3600:
            text_to_send = (f'Напоминание:\n Вы хотели {habit.action} в {habit_execution_time}\n Место'
                            f' выполнения - {habit.place}\n Выполнение займет'
                            f'{habit.time_to_complete} секунд')
            if habit.award:
                text_to_send += f'\nОбязательно побалуйте себя и можете {habit.award.reward}'

            tg_bot = TelegramNotificationBot()
            tg_bot.send_habit_notification(text_to_send, chat_id)
