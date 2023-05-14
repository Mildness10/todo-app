from django.urls import path
from todo.views import TodoListView, TodoDetailView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('todos/<int:item_id>/', TodoDetailView.as_view(), name='todo_detail')
]