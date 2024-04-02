from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='2368045max@gmail.com',
            password='Pass123',
            telegram_id=123456789
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
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
        response = self.client.delete(
            f'/users/users/{self.user.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
