from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import TodoItem
from .forms import TodoItemForm
from django.urls import reverse_lazy
# Create your views here.

class TodoListView(ListView):
    def get(self, request):
        items = TodoItem.objects.all()
        form = TodoItemForm()
        return render(request, 'todo_list.html', {'items':items, 'form':form})
    
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
    
class TodoUpdateView(UpdateView):
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo_update.html'
    
    def get_success_url(self):
        return reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
    
