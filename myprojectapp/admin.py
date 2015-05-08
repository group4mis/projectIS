from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *
from myprojectapp.forms import MyNewUserForm


class MyNewUserAdmin(admin.ModelAdmin):
    """ We inherite from the Current user and make
    some changes to it.

    """
    # we use the new form that has the account_type info
    form = MyNewUserForm

    # when overriding this function
    # you can do anything before or after saving of the model
    # the method must call obj.save() so the object can be saved
    # you can do the same thing you did in signupform before saving to
    # create the teacher, parent, or student class
    def save_model(self, request, obj, form, change):
        # do what you want here, like creating a teach and linking it
        # to the user object (which is obj)
        # form is where you will find your data
        # form.cleaned_data
        print("cleaned data {}".format(form.cleaned_data))

        # this must always be called at the end
        obj.save()


class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        'teacher_id', 'first_name', 'last_name', 'email', 'account',)
    search_fields = ('teacher_id', )


class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'student_id', 'first_name', 'last_name', 'email', 'account', 'parent')
    search_fields = ('student_id', )


class ParentsAdmin(admin.ModelAdmin):

    list_display = ('parents_id', 'email', 'account',)
    search_fields = ('parents_id', )


class StudentClassInline(admin.TabularInline):
    model = Classes.student_classses.through
    # form = MySignupForm
    # fields = ('student_id', 'first_name', 'last_name', 'email' , 'parent')


class ClassesAdmin(admin.ModelAdmin):

    list_display = ('class_id', 'class_name', 'class_semester',
                    'year', 'subject', 'grade_level', 'classes_teacher', )
    list_filter = ('class_semester', )

    exclude = ('student_classses', )

    search_fields = ('class_name', )
    inlines = [StudentClassInline]


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('attendance_id', 'student_attendance',
                    'date', 'attendancs', 'classes_attendance',)
    list_filter = ('date', )
    search_fields = ('date', )


class BehavioralNoteAdmin(admin.ModelAdmin):

    list_display = (
        'date', 'behavioral_note', 'student_behavioralnote', 'teacher_behavioralnote', )
    list_filter = ('date', )
    search_fields = ('date', )


class SpecialNoteAdmin(admin.ModelAdmin):

    list_display = ('special_note_id', 'date', 'special_note',
                    'classes_specialNote', 'teacher_specialNote', )
    list_filter = ('date', )
    search_fields = ('date', )


class GradeAdmin(admin.ModelAdmin):

    list_display = ('grade_id', 'type_g', 'total_points',
                    'grade', 'student_grade', 'classes_grade', 'total_grade')
    list_filter = ('type_g', )
    search_fields = ('type_g', )


class MeetingAdmin(admin.ModelAdmin):

    list_display = ('request_meeting_id', 'date',
                    'request_meeting', 'student_meeting', 'teacher_meeting', )
    list_filter = ('date', )
    search_fields = ('date', )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parents, ParentsAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(BehavioralNote, BehavioralNoteAdmin)
admin.site.register(SpecialNote, SpecialNoteAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Meeting, MeetingAdmin)

# let's remove the old admin for the User
admin.site.unregister(User)
# now let us register the new one we created
admin.site.register(User, MyNewUserAdmin)
