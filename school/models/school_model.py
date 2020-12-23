from django.db import models

from school.models.abstract_base_model import AbstractBaseModel


class SchoolModel(AbstractBaseModel):
    title = models.CharField(max_length=15, unique=True)
    number = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'School'

    # def __str__(self):
    #     return self.title
