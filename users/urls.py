from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    # path('student', views.student, name='student')
    
    path('meeting/',views.videocall, name='meeting'),
    path('join/',views.join_room, name='join_room'),
]