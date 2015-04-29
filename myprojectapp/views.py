from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Classes
from .models import Grade
from .models import Meeting
from .models import SpecialNote
from .models import BehavioralNote
from .models import Attendance
#Create your views here.





@login_required
def t_classes(request):
    user = request.user
    #if user.account_type=='teacher' :
    qs = Classes.objects.filter(classes_teacher__account=user)
    return render(request, "t_classes.html", {
        "user": user,
        "classes": qs,
        #if not user.account_type=='teacher'():
            #raise http.Http404
    })

@login_required
def p_classes(request):
    user = request.user
    qs = Classes.objects.filter(student_classses__parent__account=user).all
    return render(request, "p_classes.html", {
        "user": user,
        "classes": qs,
    })
@login_required
def s_classes(request):
    user = request.user
    qs = Classes.objects.filter(student_classses__account=user).all
    return render(request, "s_classes.html", {
        "user": user,
        "classes": qs,
    })
#def delete_classes(request):
#    user = request.user
#    qs = Classes.objects.filter(classes_teacher__account=user)
#    return render(request, "delete_classes.html", {
#        "user": user,
#        "classes": qs,
#        })

#def add_classes(request):

#    context = {}
#    templates = "add_classes.html"
#    return render(request, templates, context)



@login_required
def Show_Tmeetings(request):

    user = request.user
    qs = Meeting.objects.filter(teacher_meeting__account=user).all
    return render(request, "Show_Tmeetings.html", {
        "user": user,
        "Meeting": qs,
        })

@login_required
def Show_Pmeetings(request):

    user = request.user
    qs = Meeting.objects.filter(parents_meeting__account=user).all
    return render(request, "Show_Pmeetings.html", {
        "user": user,
        "Meeting": qs,
        })

@login_required
def Show_Snotes(request):

    user = request.user
    qs = SpecialNote.objects.filter(teacher_specialNote__account=user).all
    return render(request, "Show_Snotes.html", {
        "user": user,
        "SpecialNote": qs,
        })

@login_required
def Show_Bnotes(request):

    user = request.user
    qs = BehavioralNote.objects.filter(parents_behavioralnote__account=user).all
    return render(request, "Show_Bnotes.html", {
        "user": user,
        "BehavioralNote": qs,
        })


@login_required
def s_show_grade(request):
    user = request.user
    qs = Grade.objects.filter(student_grade__account=user).all
    return render(request, "s_show_grade.html", {
          "user": user,
          "Grade": qs,
        })
@login_required
def p_show_grade(request):
    user = request.user
    qs = Grade.objects.filter(student_grade__parent__account=user).all
    return render(request, "p_show_grade.html", {
          "user": user,
          "Grade": qs,
        })
@login_required
def s_show_attendance(request):
    user = request.user
    qs = Attendance.objects.filter(student_attendance__account=user).all
    return render(request, "s_show_attendance.html", {
          "user": user,
          "Attendance": qs,
        })

@login_required
def p_show_attendance(request):
    user = request.user
    qs = Attendance.objects.filter(student_attendance__parent__account=user).all
    return render(request, "p_show_attendance.html", {
          "user": user,
          "Attendance": qs,
        })

def class_details(request, class_id):
    my_class = Classes.objects.get(class_id=class_id)


def request_meeting(request, class_id):
    pass
