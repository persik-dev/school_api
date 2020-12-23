from django.urls import path

from school.views.school_api_views import SchoolCreateAPIView, SchoolRetrieveUpdateDestroyAPIView, SchoolListAPIView

urlpatterns = [
    path('<int:pk>', SchoolRetrieveUpdateDestroyAPIView.as_view()),
    path('', SchoolCreateAPIView.as_view()),
    path('list', SchoolListAPIView.as_view())
]
