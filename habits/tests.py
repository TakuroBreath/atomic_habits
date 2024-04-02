from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit, Award
from users.models import User


class HabitTestCase(APITestCase):
    """
    Test case for the Habit model and associated API views.

    Setup creates a test user with authentication and a sample Habit object.

    Attributes:
        user (User): The test user for authentication.
        client (API Client): The test client for making API requests.
        habit (Habit): A sample Habit object for testing.

    Methods:
        setUp(): Creates the test user, client, and sample Habit object.
        test_habit_create(): Tests the creation of a Habit object through the API with an invalid request.
        test_habit_list(): Tests the retrieval of a list of Habit objects through the API.
        test_habit_update(): Tests the update of a Habit object through the API with an invalid request.
        test_habit_delete(): Tests the deletion of a Habit object through the API.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user, a test client, and a sample Habit object.
        """
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
        """
        Test the creation of a Habit object through the API with an invalid request.
        """

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
        """
        Test the retrieval of a list of Habit objects through the API.
        """
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
        """
        Test the update of a Habit object through the API with an invalid request.
        """
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
        """
        Test the deletion of a Habit object through the API.
        """
        response = self.client.delete(
            f'/habit/delete/{self.habit.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class AwardTestCase(APITestCase):
    """
    Test case for the Award model and associated API views.

    Setup creates a test user with authentication and a sample Award object.

    Attributes:
        user (User): The test user for authentication.
        client (API Client): The test client for making API requests.
        award (Award): A sample Award object for testing.

    Methods:
        setUp(): Creates the test user, client, and sample Award object.
        test_award_create(): Tests the creation of an Award object through the API.
        test_award_list(): Tests the retrieval of a list of Award objects through the API.
        test_award_update(): Tests the update of an Award object through the API.
        test_award_delete(): Tests the deletion of an Award object through the API.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user, a test client, and a sample Award object.
        """
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
        """
        Test the creation of an Award object through the API.
        """

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
        """
        Test the retrieval of a list of Award objects through the API.
        """

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
        """
        Test the update of an Award object through the API.
        """

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
        """
        Test the deletion of an Award object through the API.
        """

        response = self.client.delete(
            f'/award/delete/{self.award.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
