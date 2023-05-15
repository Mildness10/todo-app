from django.urls import path
from todo.views import TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo_list'),
    path('todos/<int:item_id>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todos/<int:item_id>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('todos/<int:item_id>/delete/', TodoDeleteView.as_view(), name='todo_delete')
]