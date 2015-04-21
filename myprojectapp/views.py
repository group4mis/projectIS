from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#Create your views here.
@login_required
def base(request):
    context = {}
    templates = "base.html"
    return render(request, templates, context)


def dashboard(request):
    return render(request, "account/dashboard.html")

def teacher_classes(request):
    qs= classes.objects.all()
    return render(request, "account/teacher_classes.html", {"classes":qs})

def update_classes(request):
    return render(request, "account/update_classes.html")
