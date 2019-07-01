from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    
    try:
        projects=Projects.objects.all()
    except Exception as e:
        raise  Http404()
    return render(request,'index.html',{"projects":projects})
