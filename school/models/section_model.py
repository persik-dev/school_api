import string

from django.db import models

from school.models.abstract_base_model import AbstractBaseModel
from school.models.school_model import SchoolModel


class SectionModel(AbstractBaseModel):
    school = models.ForeignKey(
        to=SchoolModel,
        on_delete=models.CASCADE,
        related_name='sections'
    )

    section_choices = tuple(((item, item) for item in string.ascii_uppercase))
    section = models.CharField(
        choices=section_choices,
        max_length=1,
        default="A"
    )

    class Meta:
        db_table = 'Section'

    def __str__(self):
        return self.section
