from django.urls import path

from school.views.form_master_api_views import FormMasterRetrieveUpdateDestroyAPIView, FormMasterCreateAPIView, \
    FormMasterListAPIView

urlpatterns = [
    path('<int:pk>', FormMasterRetrieveUpdateDestroyAPIView.as_view()),
    path('', FormMasterCreateAPIView.as_view()),
    path('list', FormMasterListAPIView.as_view())
]
