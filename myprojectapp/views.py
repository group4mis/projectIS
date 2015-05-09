
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Classes
from .models import Grade
from .models import Meeting
from .models import SpecialNote
from .models import BehavioralNote
from .models import Attendance
from django.core.urlresolvers import reverse
from django.http import Http404
from .forms import  StudentForm, MeetingForm
from django.db.models import  Sum ,Count
#from django.http import HttpResponse, HttpResponseRedirect




#Create your views here.

@login_required
def all_classes(request):
    user = request.user

    if hasattr(user,"teacher"):
        return redirect("t_classes")

    if hasattr(user,"parents"):
        return redirect("p_classes")

    if hasattr(user,"student"):
        return redirect("s_classes")

    raise Http404


@login_required
def t_classes(request):
    user = request.user

    qs = Classes.objects.filter(classes_teacher__account=user)
    return render(request, "t_classes.html", {
        "user": user,
        "classes": qs,
    })

@login_required
def p_classes(request):
    user = request.user
    qs = Classes.objects.filter(student_classses__parent__account=user)
    return render(request, "p_classes.html", {
        "user": user,
        "classes": qs,
    })
@login_required
def s_classes(request):
    user = request.user
    qs = Classes.objects.filter(student_classses__account=user)
    return render(request, "s_classes.html", {
        "user": user,
        "classes": qs,
    })

@login_required
def show_meeting(request):
    user = request.user

    if hasattr(user,"teacher"):
        return redirect("Show_Tmeetings")

    if hasattr(user,"parents"):
        return redirect("Show_Pmeetings")

    raise Http404

@login_required
def t_show_meetings(request):

    user = request.user
    qs = Meeting.objects.filter(teacher_meeting__account=user).all
    return render(request, "t_show_meetings.html", {
        "user": user,
        "Meeting": qs,
        })

@login_required
def p_show_meetings(request):

    user = request.user
    qs = Meeting.objects.filter(student_meeting__parent__account=user).all
    return render(request, "p_show_meetings.html", {
        "user": user,
        "Meeting": qs,
        })


@login_required
def show_snotes(request):
    user = request.user

    if hasattr(user,"student"):
        return redirect("s_show_snotes")

    if hasattr(user,"parents"):
        return redirect("p_show_snotes")

    raise Http404

@login_required
def s_show_snotes(request):

    user = request.user
    qs = SpecialNote.objects.filter(classes_specialNote__student_classses__account=user).all
    return render(request, "s_show_snotes.html", {
        "user": user,
        "SpecialNote": qs,
        })
@login_required

def p_show_snotes(request):

    user = request.user
    qs = SpecialNote.objects.filter(classes_specialNote__student_classses__parent__account=user).all
    return render(request, "p_show_snotes.html", {
        "user": user,
        "SpecialNote": qs,
        })

@login_required
def show_bnotes(request):

    user = request.user
    qs = BehavioralNote.objects.filter(student_behavioralnote__parent__account=user).all
    return render(request, "show_bnotes.html", {
        "user": user,
        "BehavioralNote": qs,
        })



@login_required
def show_grade(request):
    user = request.user

    if hasattr(user,"teacher"):
        return redirect("t_classes")

    if hasattr(user,"student"):
        return redirect("s_show_grade")

    if hasattr(user,"parents"):
        return redirect("p_show_grade")

    raise Http404

@login_required
def t_show_grade(request):
    user = request.user
    qs = Grade.objects.filter(classes_grade__classes_teacher__account=user)
    return render(request, "t_show_grade.html", {
          "user": user,
          "Grade": qs,

        })


@login_required
def s_show_grade(request):
    user = request.user
    qs = Grade.objects.filter(student_grade__account=user)
    totals = qs.aggregate(total_grades=Sum('total_grade'))
    return render(request, "s_show_grade.html", {
          "user": user,
          "Grade": qs,
           "total_grades": totals["total_grades"],
         })

@login_required
def p_show_grade(request):
    user = request.user
    qs = Grade.objects.filter(student_grade__parent__account=user)
    totals = qs.aggregate(total_grades=Sum('total_grade'))
    return render(request, "p_show_grade.html", {
          "user": user,
          "Grade": qs,
          "total_grades": totals["total_grades"],
        })

@login_required
def show_attendance(request):
    user = request.user

    if hasattr(user,"teacher"):
        return redirect("t_classes")


    if hasattr(user,"student"):
        return redirect("s_show_attendance")

    if hasattr(user,"parents"):
        return redirect("p_show_attendance")

    raise Http404


@login_required
def s_show_attendance(request):
    user = request.user
    qs = Attendance.objects.filter(student_attendance__account=user).all
    #totalattendance = qs.aggregate(attendancs=Count('attendancs'))
    return render(request, "s_show_attendance.html", {
          "user": user,
          "Attendance": qs,
          #"attendancs": totalattendance["attendancs"],
        })

@login_required
def p_show_attendance(request):
    user = request.user
    qs = Attendance.objects.filter(student_attendance__parent__account=user).all
    return render(request, "p_show_attendance.html", {
          "user": user,
          "Attendance": qs,
        })

@login_required
def t_show_attendance(request):
    user = request.user
    qs = Attendance.objects.filter(classes_attendance__classes_teacher__account=user).all
    return render(request, "t_show_attendance.html", {
          "user": user,
          "Attendance": qs,
        })

@login_required
def all_classes_details(request):
    user = request.user

    if hasattr(user,"teacher"):
        return redirect("t_class_details")

    if hasattr(user,"parents"):
        return redirect("p_class_details")

    if hasattr(user,"student"):
        return redirect("s_class_details")

    raise Http404


@login_required
def t_class_details(request, class_id):

    my_class = Classes.objects.get(class_id=class_id)
    user = request.user
    countstudent = qs.aggregate(student_classses=Count('student_classses'))
    return render(request, "t_class_details.html", {
          "student_classses": countstudent ["student_classses"],
          "user": user,
          "Classes": qs,
        })


@login_required
def p_class_details(request, class_id):

    my_class = Classes.objects.get(class_id=class_id)
    user = request.user
    qs = SpecialNote.objects.filter(classes_specialNote__student_classses__parent__account=user).all
    return render(request, "p_show_snotes.html", {
        "user": user,
        "SpecialNote": qs,

    })


@login_required
def s_class_details(request, class_id):

    my_class = Classes.objects.get(class_id=class_id)
    user = request.user
    qs = SpecialNote.objects.filter(classes_specialNote__student_classses__account=user).all
    return render(request, "s_show_snotes.html", {
        "user": user,
        "SpecialNote": qs,
        })



@login_required
def p_request_meeting(request):

    user = request.user

    if request.method == "POST":
        form = MeetingForm (request.POST)
        if form.is_valid():
            form.save()
            # the product details view function looks like this
            # def product_details(request, pid):
            return redirect('p_r_m' )

    else:
        # form = MeetingForm(
        #     initial={"student_meeting":user}
        # )
        form = MeetingForm()
        form.student_meeting.queryset = Student.objects.filter(parent__account=user)

    return render(
    request,
    "p_request_meeting.html",
    {"user": user,
     "form": form,
    }
 )

@login_required
def p_r_m(request):
    user = request.user
    return render(request, "p_r_m.html", {
        "user": user,

        })


# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_email(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             RETURN HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#          In reality we'd use a form class
#          to get proper validation errors.
#        return HttpResponse('Make sure all fields are entered and valid.')
