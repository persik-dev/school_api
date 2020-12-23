from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from school.models.student_model import StudentModel


class StudentModelSerializer(WritableNestedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)


    class Meta:
        model = StudentModel
        fields = "__all__"
