from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.

class TodoListView(ListView):
    def get(self, request):
        items = TodoItem.objects.all()
        form = TodoItemForm()
        return render(request, 'todo_list.html', {"item":items, 'form':form})
    
    def post(self, request):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        items = TodoItem.objects.all()
        return render(request, 'todo_list.html', {'items':items, 'form':form})
    
class TodoDetailView(DetailView):
    def get(self, request, item_id):
        item = get_object_or_404(TodoItem, pk=item_id)
        return render(request, "todo_detail.html", {"item":item})
