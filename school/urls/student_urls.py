from django.urls import path

from school.views.student_api_views import StudentRetrieveUpdateDestroyAPIView, StudentCreateAPIView, StudentListAPIView

urlpatterns = [
    path('<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('', StudentCreateAPIView.as_view()),
    path('list', StudentListAPIView.as_view())
]
