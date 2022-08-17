from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('mysite.urls')),
    path('register/', RegisterView.as_view()),
    path('accountlist/', AccountListView.as_view()),
    path('superaccountlist/', SuperAccountListView.as_view()),
    path('courselist/', CourseListView.as_view()),
    path('applicationlist/', ApplicationView.as_view()),
    path('meetslist/', MettingView.as_view()),
    path('applicationcreate/', Onlu.as_view()),
    path('applicationmeetcreate/', ApplicationMetCreate.as_view()),
    path('grouplist/', GroupListView.as_view()),
    path('groupupdate/<int:pk>', GroupUpdateView.as_view()),
    path('grouplistbot/', GroupbotListView.as_view()),
    path('meetapplication/', MeetApplicationView.as_view()),
    path('meetapplication/<int:id>', MeetOnlyApplicationView.as_view()),
    path('applicationdelete/<int:id>', ApplicationDeleteView.as_view()),
]