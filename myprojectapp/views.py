from django.shortcuts import render
from .models import classes

# Create your views here.
 def base(request):
   context = {}
   templates = "base.html"
   return render(request, templates, context)
