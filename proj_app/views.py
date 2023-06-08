from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectsForm
from django.views.generic import DetailView

def project(request):
    project = Projects.objects.all()
    return render(request, "proj_app/project.html", {'project': project})

class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'proj_app/details_view.html'
    context_object_name = 'project'
def create(request):
    error = ''
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'
    form = ProjectsForm()

    data = {
        'form': form
    }
    return render(request, 'proj_app/create.html', data)
