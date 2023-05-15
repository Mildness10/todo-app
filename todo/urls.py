from django.urls import path
from todo.views import TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete')
]