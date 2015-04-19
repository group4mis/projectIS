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
