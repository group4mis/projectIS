from django.shortcuts import render

# Create your views here.
def base(request):
<<<<<<< HEAD
   context = {}
   templates = "base.html"
   return render(request, templates, context)
=======

   context = {}
   templates = "base.html"
   return render(request, templates, context)

def registration(request):

 return render(request, "projectis/registration.html")
>>>>>>> origin/master
