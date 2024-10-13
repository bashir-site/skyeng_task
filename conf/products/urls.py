from django.urls import path
from .views import see, add, edit, update, destroy

urlpatterns = [
    path('', see, name='see'),
    path('add', add, name='add'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='destroy'),
]
