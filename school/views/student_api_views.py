import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters

from school.models.student_model import StudentModel
from school.serializers.student_model_serializers import StudentModelSerializer


class StudentCreateAPIView(generics.CreateAPIView):
    serializer_class = StudentModelSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return StudentModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = StudentModelSerializer


class StudentListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['section', 'id']
    search_fields = ['school__title']
    filterset_fields = ['section__section']
