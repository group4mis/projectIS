from django.shortcuts import render

# Create your views here.
 def base(request):

   return HttpResponseRedirect('/registration')
   return render_to_response("base.html",locals(),context_instance_RequestContext(request))

def registration(request):

  return render_to_response("registration.html",locals(),context_instance_RequestContext(request))
