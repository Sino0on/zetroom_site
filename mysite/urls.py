from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('course_detail/<int:pk>', course_detail, name='course_detail'),
    path('application_meet/<int:pk>', applmet, name='applmeet')
]
