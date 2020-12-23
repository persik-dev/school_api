import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters

from school.models.form_master_model import FormMasterModel
from school.serializers.form_master_model_serializers import FormMasterModelSerializer


class FormMasterCreateAPIView(generics.CreateAPIView):
    serializer_class = FormMasterModelSerializer


class FormMasterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return FormMasterModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = FormMasterModelSerializer


class FormMasterListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = FormMasterModel.objects.all()
    serializer_class = FormMasterModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['id']
    search_fields = ['teacher__first_name']
    filterset_fields = ['school__title']
