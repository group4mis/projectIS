from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Classes
from .models import Grade
from .models import Meeting

#Create your views here.
@login_required
def base(request):
    user = request.user
    qs = Classes.objects.filter(classes_teacher__account=user)
    return render(request, "base.html", {
        "user": user,
        "classes": qs,
    })

def delete_classes(request):
    user = request.user
    qs = Classes.objects.filter(classes_teacher__account=user)
    return render(request, "delete_classes.html", {
        "user": user,
        "classes": qs,
        })

def add_classes(request):

    context = {}
    templates = "add_classes.html"
    return render(request, templates, context)


#def grades(request):
#    user=request.user
#    qs=grades.objects.filter(grades=user)
#    return render(request,"grades.html"{
#    "user":user
#    "grades":qs,
#    })

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
