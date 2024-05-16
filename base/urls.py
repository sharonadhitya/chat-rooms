from django.urls import path
from . import views

urlpatterns=[
    path('room/<str:q>/',views.room,name="room"), 
    path('profile/<str:q>/',views.userProfile,name="user-profile"),
    path('',views.home,name="home"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:q>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:q>/',views.deleteRoom,name="delete-room"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutpage,name="logout"),
    path('register/',views.registerpage,name="register"),
    path('delete-message/<str:q>/',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topics,name="topics"),
    path('activity/',views.activity,name="activity")
]