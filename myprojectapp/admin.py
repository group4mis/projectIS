from django.contrib import admin


# Register your models here.

from .models import *
# from myprojectapp.forms import MySignupForm

class TeacherAdmin(admin.ModelAdmin):

    list_display = ('teacher_id', 'first_name', 'last_name' ,'email','account' ,)
    search_fields = ('teacher_id', )

class StudentAdmin(admin.ModelAdmin):

    list_display = ('student_id', 'first_name', 'last_name','email','account','parent' )
    search_fields = ('student_id', )

class ParentsAdmin(admin.ModelAdmin):

    list_display = ('parents_id','email','account',)
    search_fields = ('parents_id', )


class StudentClassInline(admin.TabularInline):
    model = Classes.student_classses.through
    # form = MySignupForm
    # fields = ('student_id', 'first_name', 'last_name', 'email' , 'parent')

class ClassesAdmin(admin.ModelAdmin):

    list_display = ('class_id', 'class_name', 'class_semester' ,'year', 'subject', 'grade_level' ,'classes_teacher', )
    list_filter = ('class_semester', )

    exclude = ('student_classses', )

    search_fields = ('class_name', )
    inlines = [StudentClassInline]

class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('attendance_id', 'student_attendance','date','attendancs','classes_attendance','numder_of_absent',)
    list_filter = ('date', )
    search_fields = ('date', )

class BehavioralNoteAdmin(admin.ModelAdmin):

    list_display = ( 'date', 'behavioral_note' ,'student_behavioralnote','teacher_behavioralnote', )
    list_filter = ('date', )
    search_fields = ('date', )

class SpecialNoteAdmin(admin.ModelAdmin):

    list_display = ('special_note_id', 'date', 'special_note' ,'classes_specialNote','teacher_specialNote', )
    list_filter = ('date', )
    search_fields = ('date', )

class GradeAdmin(admin.ModelAdmin):

    list_display = ('grade_id', 'type_g', 'total_points', 'grade' , 'student_grade' ,'classes_grade','total_grade' )
    list_filter = ('type_g', )
    search_fields = ('type_g', )

class MeetingAdmin(admin.ModelAdmin):

    list_display = ('request_meeting_id', 'date', 'request_meeting' ,'student_meeting' ,'teacher_meeting', )
    list_filter = ('date', )
    search_fields = ('date', )


admin.site.register(Teacher ,TeacherAdmin)
admin.site.register(Student ,StudentAdmin)
admin.site.register(Parents,ParentsAdmin)
admin.site.register(Classes ,ClassesAdmin)
admin.site.register(Attendance ,AttendanceAdmin)
admin.site.register(BehavioralNote ,BehavioralNoteAdmin)
admin.site.register(SpecialNote ,SpecialNoteAdmin)
admin.site.register(Grade ,GradeAdmin)
admin.site.register(Meeting ,MeetingAdmin)
