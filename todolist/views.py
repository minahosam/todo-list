from django.shortcuts import redirect, render
from todolist.models import todo
from todolist.forms import TodoListForm
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
# Create your views here.
def new(request):
    tasks=todo.objects.all()
    if request.method == "POST":
        form=TodoListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')
    else:
        form=TodoListForm()
    context={'tasks':tasks , 'form':form}
    return render(request,'todolist/todolist.html',context)
def update(request,id):
    task=todo.objects.get(id=id)
    if request.method == "POST":
        form=TodoListForm(request.POST ,instance=task)
        if form.is_valid():
            form.save()
            #return redirect('/todo')\
            
    else:
        form=TodoListForm(instance=task)
        context={'form':form}
    return render(request,'todolist/update.html',context)
def delete(request,id):
    task=todo.objects.get(id=id)
    task.delete()
    return redirect ('/todo')
### class based views
class showlist(ListView):
    model=todo
    template_name='todolist/todolist1.html'
class newtodo(CreateView):
    model=todo
    template_name='todolist/todolist1.html'
    fields=['title','completed']
    success_url='/ctodo'
class update1(UpdateView):
    model=todo
    template_name='todolist/update1.html'
    fields='__all__'
    success_url='/ctodo'