from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoItem
# Create your views here.

class TodoListView(ListView):
    def get(self, request):
        items = TodoItem.objects.all()
        return render(request, 'todo_list.html', {"item":items})
    
class TodoDetailView(DetailView):
    def get(self, request):
        item = get_object_or_404(TodoItem, pk=item_id)
