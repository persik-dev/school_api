from rest_framework import serializers

from school.models.school_model import SchoolModel


class SchoolModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SchoolModel
        fields = "__all__"
