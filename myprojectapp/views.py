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

def grades(request):
    user=request.user
    qs=grades.objects.filter(grades=user)
    return render(request,"grades.html"){
    "user":user
    "grades":qs,
    }
def Show_Tmeetings(request):
    user = request.user
    qs = Meeting.objects.filter(Show_Tmeeting__account=user)
    return render(request, "Show_Tmeeting.html", {
        "user": user,
        "Show_Tmeeting": qs,
        })
def Show_Pmeetings(request):
    user = request.user
    qs = Meeting.objects.filter(Show_Pmeeting__account=user)
    return render(request, "Show_Pmeeting.html", {
        "user": user,
        "Show_Pmeeting": qs,
        })
