from django.db import models

from school.models.abstract_base_model import AbstractBaseModel


class TagModel(AbstractBaseModel):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag
