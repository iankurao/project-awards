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

def post(request):
    current_user=request.user
    if request.method=='POST':
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect("index")
    else:
        form=PostForm()
    return render(request,'post.html',{'form':form})


def profile(request):
    current_user=request.user
    try:
        profis=Profile.objects.filter(user=current_user)[0:1]
        user_projects=Projects.objects.filter(user=current_user)
    except Exception as e:
        raise  Http404()
    if request.method=='POST':
        form=UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
        return redirect('profile')
    else:
        form=UpdateForm()
    return render(request,'profile.html', {'form':form,'profile':profis,'projects':user_projects})
