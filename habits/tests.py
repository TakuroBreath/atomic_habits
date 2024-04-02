from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit, Award
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):

        existing_user = User.objects.filter(email='test@gmail.com').first()

        if existing_user:
            self.user = existing_user
        else:
            self.user = User.objects.create(
                email='test@gmail.com',
                password='test'
            )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="test_place",
            execution_time="09:15:00",
            action="run_in_gym",
            is_pleasant=False,
            parent_habit=None,
            periodic=1,
            time_to_complete=100,
            is_public=False
        )

    def test_habit_create(self):

        data = {
            "user": self.user,
            "place": "test_place",
            "award": 1,
            "execution_time": "14:10:00",
            "action": "run_in_gym",
            "is_pleasant": False,
            "parent_habit": 1,
            "periodic": 1,
            "time_to_complete": 110,
            "is_public": False
        }

        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_habit_list(self):
        response = self.client.get(
            '/habit/list/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "pk": self.habit.pk,
                        "user": self.user.email,
                        "award": None,
                        "place": "test_place",
                        "execution_time": "09:15:00",
                        "action": "run_in_gym",
                        "is_pleasant": False,
                        "parent_habit": None,
                        "periodic": 1,
                        "time_to_complete": 100,
                        "is_public": False,
                        "telegram_id": None
                    },
                ]
            }
        )

    def test_habit_update(self):
        updated_data = {
            "pk": self.habit.pk,
            "user": self.user.email,
            "award": 1,
            "place": "updated_test_place",
            "execution_time": "22:35:00",
            "action": "run_in_gym",
            "is_pleasant": False,
            "parent_habit": 2,
            "periodic": 1,
            "time_to_complete": 110,
            "is_public": False,
            "telegram_id": 1412451
        }

        response = self.client.put(
            f'/habit/update/{self.habit.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_habit_delete(self):

        response = self.client.delete(
            f'/habit/delete/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class AwardTestCase(APITestCase):

    def setUp(self):

        existing_user = User.objects.filter(email='test_award@gmail.com').first()

        if existing_user:
            self.user = existing_user
        else:
            self.user = User.objects.create(
                email='test_award@gmail.com',
                password='test_award'
            )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.award = Award.objects.create(
            user=self.user,
            reward='test_award_habit'
        )

    def test_award_create(self):

        data = {
            "user": self.user,
            "reward": "test_award_habit"
        }

        response = self.client.post(
            '/award/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_award_list(self):

        response = self.client.get(
            '/award/list/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    "pk": self.award.pk,
                    "user": str(self.user.email),
                    "reward": "test_award_habit"
                }
            ]
        )

    def test_award_update(self):

        updated_data = {
            "user": self.user.email,
            "reward": 'test_update_award'
        }

        response = self.client.put(
            f'/award/update/{self.award.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_award_delete(self):

        response = self.client.delete(
            f'/award/delete/{self.award.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
