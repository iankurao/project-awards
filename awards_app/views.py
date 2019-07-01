from django.shortcuts import render,redirect
from .forms import PostForm,RateForm,ReviewForm,UpdateForm
from .models import Projects,Rates,Comments,Profile
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
    try:
        projects=Projects.objects.all()
    except Exception as e:
        raise  Http404()
    return render(request,'index.html',{"projects":projects})
