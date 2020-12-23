from django.urls import path

from school.views.subject_api_views import SubjectRetrieveUpdateDestroyAPIView, SubjectCreateAPIView, SubjectListAPIView

urlpatterns = [
    path('<int:pk>', SubjectRetrieveUpdateDestroyAPIView.as_view()),
    path('', SubjectCreateAPIView.as_view()),
    path('list', SubjectListAPIView.as_view())
]
