import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters

from school.models.school_model import SchoolModel
from school.serializers.school_model_serializers import SchoolModelSerializer


class SchoolCreateAPIView(generics.CreateAPIView):
    serializer_class = SchoolModelSerializer


class SchoolRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return SchoolModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = SchoolModelSerializer


class SchoolListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['title', 'created_at', 'id']
    search_fields = ['title', 'address']
    filterset_fields = ['number']
