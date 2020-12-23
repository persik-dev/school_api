from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from school.models.subject_model import SubjectModel


class SubjectModelSerializer(WritableNestedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    subject = serializers.ChoiceField(choices=SubjectModel.subject_choices)

    class Meta:
        model = SubjectModel
        fields = "__all__"
