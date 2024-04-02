from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):
    """
    Test case for the User model and associated API views.

    Setup creates a sample User object.

    Attributes:
        user (User): A sample User object for testing.
        client (APIClient): The test client for making API requests.

    Methods:
        setUp(): Creates the sample User object.
        test_user_create(): Tests the creation of a User object through the API.
        test_user_list(): Tests the retrieval of a list of User objects through the API.
        test_user_update(): Tests the update of a User object through the API.
        test_user_delete(): Tests the deletion of a User object through the API.
    """

    def setUp(self):
        """
        Set up the test environment by creating a sample User object.
        """

        self.user = User.objects.create(
            email='2368045max@gmail.com',
            password='Pass123',
            telegram_id=123456789
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """
        Test the creation of a User object through the API.
        """

        data = {
            "email": "test_user@gmail.com",
            "telegram_id": 123456789,
            "password": "password123456789"
        }
        response = self.client.post(
            '/users/users/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_user_list(self):
        """
        Test the retrieval of a list of User objects through the API.
        """

        response = self.client.get(
            '/users/users/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    "pk": self.user.pk,
                    "email": self.user.email,
                    "phone": None,
                    "country": None,
                    "telegram_id": self.user.telegram_id
                }
            ]
        )

    def test_user_update(self):
        """
        Test the update of a User object through the API.
        """

        updated_data = {
            "email": self.user.email,
            "phone": "+123456789",
            "country": "test_country",
            "telegram_id": self.user.telegram_id
        }

        response = self.client.put(
            f'/users/users/{self.user.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_delete(self):
        """
        Test the deletion of a User object through the API.
        """

        response = self.client.delete(
            f'/users/users/{self.user.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
