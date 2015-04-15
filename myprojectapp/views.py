from django.shortcuts import render

# Create your views here.
def base(request):
   context = {}
   templates = "base.html"
   return render(request, templates, context)
