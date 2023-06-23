from django.contrib import admin
from django.urls import path
from app.views import home,login,signup,add_todo,signout,delete,status
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('add-todo/',add_todo,name="add-todo"),
    path('logout/',signout,name="logout"),
    path('delete-todo/<int:id>',delete,name="delete"),
    path('change-status/<int:id>/<str:status>',status,name="status"),
]
