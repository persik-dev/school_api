from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from school.models.teacher_model import TeacherModel
from school.serializers.tag_model_serializer import TagModelSerializer


class TeacherModelSerializer(WritableNestedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    currently_working = serializers.BooleanField(read_only=True)
    tags = TagModelSerializer(many=True)

    class Meta:
        model = TeacherModel
        fields = "__all__"
