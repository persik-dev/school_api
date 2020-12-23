from django.urls import path

from school.views.section_api_views import SectionRetrieveUpdateDestroyAPIView, SectionCreateAPIView, SectionListAPIView

urlpatterns = [
    path('<int:pk>', SectionRetrieveUpdateDestroyAPIView.as_view()),
    path('', SectionCreateAPIView.as_view()),
    path('list', SectionListAPIView.as_view())
]
