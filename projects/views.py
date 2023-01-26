from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm


# Create your views here.
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {"list_projects": project_list}
    return render(request, "projects/project_list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/project_create.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {"project": project}
    return render(request, "projects/project_detail.html", context)
