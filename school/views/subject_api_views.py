import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters

from school.models.subject_model import SubjectModel
from school.serializers.subject_model_serializers import SubjectModelSerializer


class SubjectCreateAPIView(generics.CreateAPIView):
    serializer_class = SubjectModelSerializer


class SubjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return SubjectModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = SubjectModelSerializer


class SubjectListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['subject', 'id']
    search_fields = ['school__title']
    filterset_fields = ['school__title', 'teacher__first_name']
