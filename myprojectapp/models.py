
from django.db import models
from django.conf import settings

# Create your models here.

def get_account_type(user):
    if user.parent:
       return "parent"

    if user.student:
       return "student"

    if user.teacher:
       return "teacher"

    return "unknown type"

class Teacher(models.Model):

  teacher_id = models.CharField(max_length=20,unique=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=30)
  account = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
  def __unicode__(self):
    return u"{}, {} {}".format(self.account.username, self.first_name , self.last_name )

class Student(models.Model):

  student_id = models.CharField(max_length=20,unique=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=30)
  account = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
  parent = models.ForeignKey('Parents', blank=True)

  def __unicode__(self):
    return u"{}, {}".format(self.account.username , self.student_id )

class Parents(models.Model):

  parents_id = models.CharField(max_length=20,unique=True)
  email = models.EmailField(max_length=30)
  account = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)


  def __unicode__(self):
    return u"{}, {}, {} , {} {}".format(self.account.username , self.parents_id , self.parent_student.student_id ,self.parent_student.first_name , self.parent_student.last_name)

class Classes(models.Model):

  class_id = models.CharField(max_length=20,unique=True)
  class_name = models.CharField(max_length=30,unique=True)
  class_semester = models.CharField(max_length=30,blank=True)
  year= models.CharField(max_length=30,blank=True)
  subject = models.CharField(max_length=30)
  grade_level = models.IntegerField(max_length=30)
  classes_teacher= models.ForeignKey(Teacher, blank=True, null=True)
  student_classses=models.ManyToManyField('Student', blank=True)


  def __unicode__(self):
    return u"{},{}".format ( self.classes_teacher.teacher_id ,self.class_name)

class Attendance(models.Model):
  attendance_id = models.CharField(max_length=30,unique=True)
  student_attendance = models.ForeignKey(Student, blank=True, null=True)
  classes_attendance = models.ForeignKey(Classes, blank=True, null=True)
  date = models.DateField()
  attendancs = models.NullBooleanField()
  def __unicode__(self):
    return u"{},{} {} ,{}".format ( self.student_attendance.student_id ,self.student_attendance.first_name ,self.student_attendance.last_name , self.classes_attendance.class_name)

class BehavioralNote(models.Model):

  behavioral_note_id = models.IntegerField(max_length=30,unique=True)
  date = models.DateField()
  behavioral_note  = models.TextField(max_length=300,)
  parents_behavioralnote= models.ForeignKey(Parents, blank=True, null=True)
  teacher_behavioralnote = models.ForeignKey(Teacher, blank=True, null=True)
  def __unicode__(self):
    return u"{},{},{} {}".format ( self.parents_behavioralnote.parent_student ,  self.parents_behavioralnote.account , self.teacher_behavioralnote.first_name , self.teacher_behavioralnote.last_name)

class SpecialNote(models.Model):

  special_note_id = models.IntegerField(max_length=30,unique=True)
  date = models.DateField()
  special_note  = models.TextField(max_length=300)
  classes_specialNote = models.ForeignKey(Classes, blank=True, null=True)
  teacher_specialNote = models.ForeignKey(Teacher, blank=True, null=True)
  def __unicode__(self):
        return u"{},{} {}".format ( self.classes_specialNote.class_name, self.teacher_specialNote.first_name , self.teacher_specialNote.last_name)

class Grade(models.Model):

  grade_id = models.CharField(max_length=30,unique=True)
  type_g = models.CharField(max_length=30)
  grade = models.CharField(max_length=30)
  total_points = models.CharField(max_length=30)
  student_grade = models.ForeignKey(Student, blank=True, null=True)
  classes_grade = models.ForeignKey(Classes, blank=True, null=True)
  def __unicode__(self):
    return u"{}, {} ,{}  {}".format ( self.classes_grade.class_name , self.student_grade.student_id ,self.student_grade.first_name ,self.student_grade.last_name )

class Meeting(models.Model):

  request_meeting_id = models.IntegerField(max_length=30,unique=True)
  date = models.DateField()
  request_meeting  = models.TextField(max_length=300)
  parents_meeting = models.ForeignKey(Parents,blank=True, null=True)
  teacher_meeting = models.ForeignKey(Teacher,blank=True, null=True)

  def __unicode__(self):
    return u"{},{} {}".format ( self. parents_meeting.parent_student, self.teacher_meeting.first_name , self.teacher_meeting.last_name)
