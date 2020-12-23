from rest_framework import serializers

from school.models.tag_model import TagModel


class TagModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    def is_valid(self, raise_exception=False):
        if hasattr(self, 'initial_data'):
            try:
                tag = self.Meta.model.objects.get(**self.initial_data)
            except (self.Meta.model.DoesNotExist, self.Meta.model.MultipleObjectsReturned):
                return super().is_valid(raise_exception=True)
            else:
                self.instance = tag
                return super().is_valid(raise_exception=True)
        else:
            return super().is_valid(raise_exception=True)

    class Meta:
        model = TagModel
        fields = "__all__"
