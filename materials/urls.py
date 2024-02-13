from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet
from materials.views import LessonListAPIView, LessonDestroyAPIView, LessonUpdateAPIView, LessonRetriaveAPIView, LessonCreateAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/', LessonRetriaveAPIView.as_view(), name='lesson_info'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),

              ] + router.urls
