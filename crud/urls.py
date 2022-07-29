from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', create_view),
    path('list/', list_view , name="list"),
    path('detail/<int:id>/', detail_view),
    path('update/<int:id>/', update_view),
    path('delete/<int:id>/', delete_view),
   
]