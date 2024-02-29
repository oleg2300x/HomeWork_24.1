from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import UrlValidator
from subscription.models import Subscriptions


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "url"]
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson", many=True, read_only=True)
    course_subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        return len(instance.lesson.all())

    def get_course_subscription(self, instance):
        subscription = Subscriptions.objects.all().filter(course=instance.pk).filter(
            user=self.context.get('request').user.pk)
        if subscription:
            return True
        else:
            return False





