from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from school.models.form_master_model import FormMasterModel


class FormMasterModelSerializer(WritableNestedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    grade = serializers.ChoiceField(choices=FormMasterModel.grade_choices)

    class Meta:
        model = FormMasterModel
        fields = "__all__"
