from django.http import JsonResponse
from django.shortcuts import render

from .forms import ToDoForm
from .models import Todo


def index(request):
    todo = Todo.objects.all()
    todoForm = ToDoForm()

    return render(request, 'todolist/todo.html', {'todo': todo, 'todoForm': todoForm})


def saveTask(request):
    if request.method == 'POST':
        todoForm = ToDoForm(request.POST)

        if todoForm.is_valid():
            taskid = request.POST.get('taskid')

            if taskid == "":
                todoForm.save(commit=True)
            else:
                taskEdit = Todo.objects.get(pk=taskid)
                taskSave = ToDoForm(request.POST, instance=taskEdit)
                taskSave.save(commit=True)

            todo = Todo.objects.values()
            todoData = list(todo)

            return JsonResponse({'status': 1, 'todoData': todoData})
        else:
            return JsonResponse({'status': 0})


def deleteTask(request):
    if request.method == "POST":
        id = request.POST.get('sid')

        task = Todo.objects.get(pk=id)
        task.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def editTask(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        task = Todo.objects.get(pk=id)
        task_data = {"id": task.id, "task": task.todo}
        return JsonResponse(task_data)
