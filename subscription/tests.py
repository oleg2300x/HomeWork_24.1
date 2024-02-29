from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from subscription.models import Subscriptions
from materials.models import Course


class SubscriptionAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="testuser@test,com",
            phone="12345",
            country="testcity",
            password='12345'
        )
        self.course = Course.objects.create(
            id=10,
            title="CourseTest 1",
            description="CourseDescroption 1",
            owner=self.user
        )

    def test_create_subscriptions(self):
        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/subscriptions/',
            data=data)

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
