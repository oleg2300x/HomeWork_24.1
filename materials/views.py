from datetime import datetime

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from materials.utils import get_url_for_payment
from rest_framework.response import Response

from materials.models import Course, Lesson
from materials.pagination import CoursePagination, LessonPagination
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer
from payment.models import Payment


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.user = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    queryset = Lesson.objects.all()


class LessonRetriaveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Lesson.objects.all()


class CoursePaymentAPIView(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]

        course_item = get_object_or_404(Course, pk=course_id)

        if course_item:
            url_for_payment = get_url_for_payment(course_item)
            message = 'Для оплаты нажмите на ссылку'
            data = {
                "user": user,
                "date": datetime.now(),
                "course": course_item,
                "amount": course_item.price,
                "method": "T",
                "url_for_payment": url_for_payment,
                "status": "P",
            }
            payment = Payment.objects.create(**data)
            payment.save()
            return Response({"message": message, "url": url_for_payment})
        else:
            message = 'Курс с таким ID не найден'
            return Response({"message": message})