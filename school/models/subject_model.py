from django.db import models

from school.models.abstract_base_model import AbstractBaseModel
from school.models.school_model import SchoolModel
from school.models.teacher_model import TeacherModel


class SubjectModel(AbstractBaseModel):
    subjects_list = [
        "Art", "Citizenship", "Geography", "History", "French",
        "German", "Spanish", "Literacy", "Music", "Natural", "Science",
        "Arithmetic", "Social", "Studies", "Reading", "Writing"
    ]

    subject_choices = tuple((item, item) for item in subjects_list)

    subject = models.CharField(
        max_length=25,
        choices=subject_choices,
        default="Art"
    )

    teacher = models.ManyToManyField(
        to=TeacherModel,
        related_name='subjects'
    )

    school = models.ForeignKey(
        to=SchoolModel,
        on_delete=models.CASCADE,
        default=0,
        related_name='subjects'
    )

    class Meta:
        db_table = 'Subject'

    def __str__(self):
        return self.subject
