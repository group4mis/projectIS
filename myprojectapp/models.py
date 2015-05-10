from django.db import models
from django.conf import settings

#from django.core.email import send_mail

# Create your models here.


def get_account_type(user):
    if user.parents:
        return "parents"

    if user.student:
        return "student"

    if user.teacher:
        return "teacher"

    return "unknown type"


class Teacher(models.Model):

    def next_teacher_id():

        no = Teacher.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    teacher_id = models.IntegerField(
        max_length=30, unique=True, default=next_teacher_id, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        return u"{}, {} {}".format(self.account.username, self.first_name, self.last_name)


class Student(models.Model):

    def next_student_id():

        no = Student.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    student_id = models.IntegerField(
        max_length=30, unique=True, default=next_student_id, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True)
    parent = models.ForeignKey('Parents',blank=True)

    def __unicode__(self):
        return u"{},{}".format(self.account.username, self.parent.account.username)


class Parents(models.Model):

    def next_parents_id():

        no = Parents.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    parents_id = models.IntegerField(
        max_length=30, unique=True, default=next_parents_id, editable=False)
    email = models.EmailField(max_length=30)
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        return u"{},{}".format(self.parents_id , self.account.username)


class Classes(models.Model):

    def number():

        no = Classes.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    class_id = models.IntegerField(
        max_length=30, unique=True, default=number, editable=False)
    class_name = models.CharField(max_length=30, unique=True)
    class_semester = models.CharField(max_length=30, blank=True)
    year = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=30)
    grade_level = models.IntegerField(max_length=30)
    classes_teacher = models.ForeignKey(Teacher, blank=True, null=True)
    student_classses = models.ManyToManyField('Student', blank=True)

    def __unicode__(self):
        return u"{},{},{}".format(self.classes_teacher.account.username, self.class_name,self.class_id)


class Attendance(models.Model):

    def id_number():

        no = Attendance.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    # def no_of_absent():
    #
    #     if Attendance == "NO":
    #        number_of_absent = Attendance.objects.count()
    #        if number_of_absent == None:
    #             return 0
    #        else:
    #             return number_of_absent + 1

    attendance_id = models.IntegerField(
        max_length=30, unique=True, default=id_number, editable=False)
    student_attendance = models.ForeignKey(Student, blank=True, null=True)
    classes_attendance = models.ForeignKey(Classes, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    attendancs = models.NullBooleanField()
    numder_of_absent= models.CharField(max_length=30)

    def __unicode__(self):
        return u"{} {} ,{}".format(self.student_attendance.first_name, self.student_attendance.last_name, self.classes_attendance.class_name)


class BehavioralNote(models.Model):

    def number():

        no = BehavioralNote.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    behavioral_note_id = models.IntegerField(
        max_length=30, unique=True, default=number, editable=False)
    date = models.DateField(auto_now_add=True)
    behavioral_note = models.TextField(max_length=300,)
    student_behavioralnote = models.ForeignKey(Student, blank=True, null=True)
    teacher_behavioralnote = models.ForeignKey(Teacher, blank=True, null=True)
    deducted_points = models.CharField(max_length=30, blank=False, null=False)

    def __unicode__(self):
        return u"{} {} will be deducted ({})".format(self.student_behavioralnote.first_name, self.student_behavioralnote.last_name, self.deducted_points)


class SpecialNote(models.Model):

    def number():

        no = SpecialNote.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    special_note_id = models.IntegerField(
        max_length=30, unique=True, default=number, editable=False)
    date = models.DateField(auto_now_add=True)
    special_note = models.TextField(max_length=300)
    classes_specialNote = models.ForeignKey(Classes, blank=True, null=True)
    teacher_specialNote = models.ForeignKey(Teacher, blank=True, null=True)

    def __unicode__(self):
        return u"{},{} {}".format(self.classes_specialNote.class_name, self.teacher_specialNote.first_name, self.teacher_specialNote.last_name)


class Grade(models.Model):

    def number():

        no = Grade.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    grade_id = models.CharField(
        max_length=30, unique=True, default=number, editable=False)
    type_g = models.CharField(max_length=30)
    total_points = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    total_grade = models.CharField(max_length=30)
    student_grade = models.ForeignKey(Student, blank=True, null=True)
    classes_grade = models.ForeignKey(Classes, blank=True, null=True)
    deducted_points_grade = models.ForeignKey(
        BehavioralNote, blank=False, null=False, max_length=30)

    def __unicode__(self):
        return u"{} {}".format(self.student_grade.first_name, self.student_grade.last_name)


class Meeting(models.Model):

    def number():
        no = Meeting.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    request_meeting_id = models.IntegerField(
        max_length=30, unique=True, default=number, editable=False)
    date = models.DateField(auto_now_add=True)
    request_meeting = models.TextField(max_length=300)
    student_meeting = models.ForeignKey(Student, blank=True, null=True)
    teacher_meeting = models.ForeignKey(Teacher, blank=True, null=True)

    def __unicode__(self):
        return u"{},{} {}".format(self. student_meeting.parent.account.username, self.teacher_meeting.first_name, self.teacher_meeting.last_name)
