from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone
from .forms import TaskForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def view_tasks(request):
    all_tasks = Task.objects.order_by('-create_time')
    users = User.objects.all()

    #pass the user to html
    user = request.user.username

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Add a task':
            return redirect('add-task')
        
    title_filter = request.GET.get('title')
    if title_filter:
        if title_filter != "None":
            tasks = all_tasks.filter(id=title_filter)
        else:
            tasks = all_tasks
    else:
        tasks = all_tasks

    assigned_person_filter = request.GET.get('assigned_person')
    if assigned_person_filter:
        print(assigned_person_filter)
        if assigned_person_filter != "None":
            tasks = tasks.filter(user__id=assigned_person_filter)

    context = {'tasks': tasks, 'logged_user': user, 'allTasks': all_tasks, 'users': users}

    return render(request, 'tasks/view_tasks.html', context)

@login_required
def add_task(request):
    if request.method == 'POST':   

        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.create_time = timezone.now()

            selected_user = task_form.cleaned_data['user']

            if selected_user:
                task.user = selected_user
            else:
                task.user = None

            task.save()
            # breakpoint()
            return redirect('view_tasks')
        else:
            context = {'form': task_form}
            return render(request, 'tasks/add_tasks.html', context)
    else:
        task_form = TaskForm()
        context = {'form': task_form}
        return render(request, 'tasks/add_tasks.html', context)
    
@login_required
def get_task(request, id):
    task = get_object_or_404(Task, id=id)

    isUserAdmin = request.user.is_superuser

    # only the person to which task is assigned or an admin can change the description of the task
    doesTaskBelongToUser = False
    if task.user == request.user:
        doesTaskBelongToUser = True

    # breakpoint()
    context = {'task': task, "isUserAdmin": isUserAdmin, "doesTaskBelongToUser": doesTaskBelongToUser}

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'edit':
            return redirect('edit_task',id=task.id)
        elif action == 'delete':
            task.delete()
            return redirect('view_tasks')


    return render(request, 'tasks/view.html', context)

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  
            return redirect('view_tasks')
        
    else:
        # Pre-populate the form with the current data of the news article
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form})