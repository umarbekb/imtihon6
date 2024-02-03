from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from .models import GeeksModel
from .forms import GeeksForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def search_todos(request):
    query = request.GET.get('q')
    todos = Todo.objects.filter(title__icontains=query)
    return render(request, 'todo/search_results.html', {'todos': todos})


def filter_todos(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    todos = Todo.objects.filter(due_date__range=[start_date, end_date])
    return render(request, 'todo/filter_results.html', {'todos': todos})


def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)
