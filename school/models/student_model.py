from django.db import models

from school.models.abstract_base_model import AbstractBaseModel
from school.models.school_model import SchoolModel
from school.models.section_model import SectionModel


class StudentModel(AbstractBaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    school = models.ForeignKey(
        to=SchoolModel,
        on_delete=models.CASCADE,
        related_name='students'
    )

    section = models.ForeignKey(
        to=SectionModel,
        on_delete=models.SET_NULL,
        related_name='students',
        null=True
    )

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return self.first_name
