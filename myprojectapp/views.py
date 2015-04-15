from django.shortcuts import render

# Create your views here.
def base(request):
<<<<<<< HEAD
   context = {}
   templates = "base.html"
   return render(request, templates, context)
=======

   return HttpResponseRedirect('/registration')
   return render_to_response("base.html",locals(),context_instance_RequestContext(request))

def registration(request):

 return render(request, "projectis/registration.html")
>>>>>>> origin/master
