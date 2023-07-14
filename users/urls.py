from django.urls import path
from .views import CustomUserCreate, UserList

app_name = 'users'

urlpatterns = [
    path('list/', UserList.as_view(), name="user_list"),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
]
