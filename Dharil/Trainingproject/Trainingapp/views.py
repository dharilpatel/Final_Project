from django.shortcuts import render, HttpResponse, HttpResponseRedirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from  django.contrib import auth

from forms import SignupForm



# Create your views here.
def Home(request):
    return HttpResponse("Hey !! WHats up ??")

def signup(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("User Created !!")
            return ren
    else:
        form = SignupForm()
        print form
    return render(request,'signup.html',{'form': form}, c)

def login(request):
    c = {}
    #c.update(csrf(request))
    return render_to_response('registration/login.html',c, content_type= "registraion/login.html")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponse("Logged In")
    else:
        return HttpResponse("Invalid credentials")
