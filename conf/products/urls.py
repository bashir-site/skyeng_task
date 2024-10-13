from django.urls import path, include
from .views import see, add, edit, update, destroy, register, user_login, user_logout

urlpatterns = [
    path('', see, name='see'),
    path('add', add, name='add'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='destroy'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
