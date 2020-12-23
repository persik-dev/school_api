from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from school.models.section_model import SectionModel


class SectionModelSerializer(WritableNestedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    section = serializers.ChoiceField(choices=SectionModel.section_choices)

    class Meta:
        model = SectionModel
        fields = "__all__"
