import django_filters.rest_framework as drf_filters
from rest_framework import generics, filters, status
from rest_framework.response import Response

from school.models.teacher_model import TeacherModel
from school.serializers.teacher_model_serializers import TeacherModelSerializer


class TeacherCreateAPIView(generics.CreateAPIView):
    """
    Для tags сделано так чтоб работало по get_or_create() вместо стандартного create()
    посредством кастомизации (override) метода is_valid() в TagModelSerializer.
    Посмотрите в .../school/serializers/tag_model_serializer.py
    """
    serializer_class = TeacherModelSerializer


class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return TeacherModel.objects.filter(id=self.kwargs["pk"])

    serializer_class = TeacherModelSerializer

    """
    Допустим мы хотим применить soft delete. 
    Делаем override метода destroy. 
    """

    def destroy(self, request, *args, **kwargs):
        if self.get_queryset():
            self.get_queryset().update(currently_working=False)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class TeacherListAPIView(generics.ListAPIView):
    """
    Фильтруем, сортируем, используем поиск
    """
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherModelSerializer
    filter_backends = [
        drf_filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    ordering_fields = ['first_name', 'last_name', 'id']
    search_fields = ['first_name', 'last_name', 'school__title']
    filterset_fields = ['currently_working']
