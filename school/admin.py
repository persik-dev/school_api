from django.contrib import admin

from school.models.form_master_model import FormMasterModel
from school.models.school_model import SchoolModel
from school.models.section_model import SectionModel
from school.models.student_model import StudentModel
from school.models.subject_model import SubjectModel
from school.models.teacher_model import TeacherModel

register = admin.site.register
register(SchoolModel)
register(TeacherModel)
register(SubjectModel)
register(StudentModel)
register(SectionModel)
register(FormMasterModel)
