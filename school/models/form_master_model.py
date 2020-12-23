from django.db import models

from school.models.abstract_base_model import AbstractBaseModel
from school.models.school_model import SchoolModel
from school.models.section_model import SectionModel
from school.models.teacher_model import TeacherModel


class FormMasterModel(AbstractBaseModel):
    grade_choices = tuple((str(item), item) for item in range(13))

    school = models.ForeignKey(
        to=SchoolModel,
        on_delete=models.CASCADE,
        related_name='form_master'
    )

    teacher = models.OneToOneField(
        to=TeacherModel,
        on_delete=models.CASCADE,
        related_name='form_master'
    )

    section = models.ForeignKey(
        to=SectionModel,
        on_delete=models.CASCADE,
        related_name='form_master'
    )

    grade = models.PositiveIntegerField(
        choices=grade_choices,
        default=0
    )

    class Meta:
        db_table = 'Form Master'

    def __str__(self):
        return self.teacher.first_name
