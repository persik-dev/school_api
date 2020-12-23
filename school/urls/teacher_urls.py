from django.urls import path

from school.views.teacher_api_views import TeacherRetrieveUpdateDestroyAPIView, TeacherListAPIView, TeacherCreateAPIView

urlpatterns = [
    path('<int:pk>', TeacherRetrieveUpdateDestroyAPIView.as_view()),
    path('', TeacherCreateAPIView.as_view()),
    path('list', TeacherListAPIView.as_view())
]
