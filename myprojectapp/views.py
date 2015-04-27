from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Classes
from .models import Grade
from .models import Meeting
from .models import SpecialNote
from .models import BehavioralNote
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


def class_details(request, class_id):
    my_class = Classes.objects.get(class_id=class_id)
    pass

def request_meeting(request, class_id):
    pass
