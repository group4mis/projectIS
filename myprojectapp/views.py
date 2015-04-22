from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Classes

#Create your views here.
@login_required
def base(request):
    user = request.user
    qs = Classes.objects.filter(classes_teacher__account=user)
    return render(request, "base.html", {
        "user": user,
        "classes": qs,
    })

def update_class(request):
    context = {}
    templates = "Update_class.html"
    return render(request, templates, context)

def add_classes(request):

    context = {}
    templates = "add_classes.html"
    return render(request, templates, context)
