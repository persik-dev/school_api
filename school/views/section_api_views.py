import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters

from school.models.section_model import SectionModel
from school.serializers.section_serializers import SectionModelSerializer


class SectionCreateAPIView(generics.CreateAPIView):
    serializer_class = SectionModelSerializer


class SectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return SectionModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = SectionModelSerializer


class SectionListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = SectionModel.objects.all()
    serializer_class = SectionModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['section', 'id']
    search_fields = ['school__title']
    filterset_fields = ['section']
