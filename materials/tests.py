from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class CourseAPITest(APITestCase):

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
        self.lesson = Lesson.objects.create(
            id=1,
            title="LessonTest 1",
            description="Lesson Discription Test",
            url="youtube.com",
            Course=self.course,
            owner=self.user
        )

    def test_get_list_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/course/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_course(self):
        data = {
            "title": "CourseTest 2",
            "description": "CourseDescroption 2",
            "owner": self.user.pk
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/course/',
            data=data)

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/course/10/')

        # print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_get_list_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/lesson/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {
            "title": "LessonTest 2",
            "description": "Lesson Discription Test 2",
            "owner": self.user.pk,
            "url": "youtube.com",
        }
        print(data)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/course/',
            data=data)
        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        responce = self.client.delete(
            '/lesson/delete/1/')
        print(Lesson.objects.all())

        self.assertEquals(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
        )
