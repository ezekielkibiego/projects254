from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

def index(request):
    
    projects = Project.objects.all().order_by('-id')
    return render(request, 'index.html', {'projects': projects})

def add_project(request):
    projects = Project.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = request.user
            projects.save()
            return redirect('index')
    
    else:
        form = ProjectForm() 
    return render (request, 'add_project.html', {'form':form, 'projects':projects})