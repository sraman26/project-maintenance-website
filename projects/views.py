from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {"list_projects": project_list}
    return render(request, "projects/project_list.html", context)
