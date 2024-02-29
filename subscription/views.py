from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Course
from subscription.models import Subscriptions
from django.shortcuts import get_object_or_404


class SubscribeAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        try:
            course_id = self.request.data["course"]
        except KeyError:
            return Response({"error": "Missing 'course' parameter"}, status=status.HTTP_400_BAD_REQUEST)
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscriptions.objects.filter(user=user).filter(course=course_id).all()
        course_name = course_item.title

        if len(subs_item) > 0:
            subscription_id = subs_item[0].pk
            subscription = Subscriptions.objects.get(pk=subscription_id)
            subscription.delete()
            message = 'Подписка удалена '
        else:
            new_subscription = {
                "user": user,
                "course_id": course_id
            }
            Subscriptions.objects.create(**new_subscription)
            message = 'подписка добавлена'
        return Response(f'Пользователь: {user}.'
                        f' (Курс - {course_name} - {message})')