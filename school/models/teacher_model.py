from django.db import models

from school.models.abstract_base_model import AbstractBaseModel
from school.models.school_model import SchoolModel
from school.models.tag_model import TagModel


class TeacherModel(AbstractBaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    currently_working = models.BooleanField(default=True)

    school = models.ManyToManyField(
        to=SchoolModel,
        related_name='teachers'
    )

    tags = models.ManyToManyField(to=TagModel)

    class Meta:
        db_table = 'Teacher'

    def __str__(self):
        return self.first_name
